import os
import time
import base64
import json
import cv2
import numpy as np
from dotenv import load_dotenv
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Load BrowserStack credentials
load_dotenv()
USERNAME = os.getenv("BROWSERSTACK_USERNAME")    
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")  

if not USERNAME or not ACCESS_KEY:
    raise ValueError("❌ BROWSERSTACK_USERNAME or BROWSERSTACK_ACCESS_KEY is missing from environment variables!")

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Devices for testing
DEVICES = [
    {"device": "Samsung Galaxy S22", "os_version": "12.0", "browser": "Chrome"},
    {"device": "iPhone 14", "os_version": "16.0", "browser": "Safari"},
]

# Test URL & Screenshot Storage
TEST_URL = "https://eatanceapp.com/"
SCREENSHOT_DIR = os.path.abspath("screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

BASELINE_DEVICE = "Samsung Galaxy S22"
baseline_screenshot = None
results = []

def get_driver(config):
    """Initialize BrowserStack WebDriver."""
    capabilities = {
        "browserstack.user": USERNAME,
        "browserstack.key": ACCESS_KEY,
        "browserstack.debug": "true",
        "browserstack.networkLogs": "true",
        **config
    }
    options = Options()
    for key, value in capabilities.items():
        options.set_capability(key, value)
    return webdriver.Remote(command_executor=BROWSERSTACK_URL, options=options)

def capture_full_page_screenshot(driver, name):
    """Scroll and capture full-page screenshots manually."""
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}_full.png")
    
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    full_width = driver.execute_script("return document.documentElement.scrollWidth")  

    stitched_image = Image.new('RGB', (full_width, total_height))  

    scroll_position = 0
    part = 0
    part_images = []

    while scroll_position < total_height:
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(2)  

        part_path = os.path.join(SCREENSHOT_DIR, f"{name}_part{part}.png")
        driver.save_screenshot(part_path)
        part_img = Image.open(part_path).convert("RGB")
        
        # Ensure width consistency
        part_img = part_img.resize((full_width, part_img.height), Image.Resampling.LANCZOS)

        part_images.append((part_img, scroll_position))
        scroll_position += viewport_height
        part += 1

    # Merge images properly
    for img, y_offset in part_images:
        stitched_image.paste(img, (0, y_offset))
    
    stitched_image.save(screenshot_path)
    print(f"✅ Full-page screenshot saved: {screenshot_path}")
    return screenshot_path



def compare_images(baseline_path, test_path, output_path):
    """Compares two images and highlights differences."""
    baseline = Image.open(baseline_path).convert("RGB")
    test = Image.open(test_path).convert("RGB")
    
    if baseline.size != test.size:
        test = test.resize(baseline.size)
    
    diff = ImageChops.difference(baseline, test)
    bbox = diff.getbbox()
    
    if bbox:
        # Convert images to OpenCV format
        baseline_cv = cv2.cvtColor(np.array(baseline), cv2.COLOR_RGB2BGR)
        test_cv = cv2.cvtColor(np.array(test), cv2.COLOR_RGB2BGR)
        
        # Find differences using OpenCV
        diff_gray = cv2.cvtColor(cv2.absdiff(baseline_cv, test_cv), cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(diff_gray, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw bounding boxes for differences
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(test_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red for differences
            cv2.rectangle(baseline_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green for correct areas
        
        # Save updated images
        compared_path = os.path.join(output_path, "compared.png")
        cv2.imwrite(compared_path, test_cv)
        
        return True, compared_path  # Differences found
    
    return False, baseline_path  # No differences found

def run_tests():
    """Run UI tests on all devices and store results for reporting."""
    global baseline_screenshot
    for device in DEVICES:
        device_name = device["device"]
        print(f"🚀 Testing on: {device_name}")
        
        driver = get_driver(device)
        driver.get(TEST_URL)
        time.sleep(5)

        try:
            screenshot_path = capture_full_page_screenshot(driver, device_name)
        except Exception as e:
            print(f"❌ Screenshot capture failed: {e}")
            driver.quit()
            continue  # Skip this test if we fail to capture a screenshot

        if device_name == BASELINE_DEVICE:
            baseline_screenshot = screenshot_path
            print(f"📌 Baseline screenshot set for {BASELINE_DEVICE}")
        else:
            # Compare with baseline and store results
            has_diff, diff_path = compare_images(baseline_screenshot, screenshot_path, SCREENSHOT_DIR)

            # Determine border color based on comparison
            border_color = "red" if has_diff else "green"
            status_text = "Differences Found" if has_diff else "No Differences"

            results.append({
                "device": device_name,
                "baseline_image": baseline_screenshot,
                "test_image": screenshot_path,
                "diff_image": diff_path,
                "border": border_color,
                "status": status_text
            })
        
        driver.quit()
    
    generate_html_report()

def generate_html_report():
    """Generate an HTML report with comparison results."""
    if not results:
        print("⚠️ No results to generate report!")
        return
    
    report_path = os.path.join(SCREENSHOT_DIR, "ui_test_report.html")
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>UI Test Report</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; }
            table { width: 100%; border-collapse: collapse; background: white; }
            th, td { padding: 10px; border: 1px solid black; text-align: center; }
            img { max-width: 300px; display: block; margin: 0 auto; }
        </style>
    </head>
    <body>
        <h1>UI Test Report</h1>
        <table>
            <tr>
                <th>Device</th>
                <th>Baseline Screenshot</th>
                <th>Test Screenshot</th>
                <th>Difference</th>
                <th>Status</th>
            </tr>
    """
    for result in results:
        html_content += f"""
        <tr>
            <td>{result['device']}</td>
            <td><img src="file:///{result['baseline_image']}" alt="Baseline"></td>
            <td><img src="file:///{result['test_image']}" alt="Test"></td>
            <td><img src="file:///{result['diff_image']}" alt="Difference"></td>
            <td style="border: 3px solid {result['border']};">{result['status']}</td>
        </tr>
        """
    
    html_content += "</table></body></html>"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"📄 Report generated: {report_path}")

if __name__ == "__main__":
    run_tests()
