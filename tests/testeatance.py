import os
import time
import cv2
import numpy as np
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()
import logging
from selenium.webdriver.common.by import By

BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")    
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")  

if not BROWSERSTACK_USERNAME or not BROWSERSTACK_ACCESS_KEY:
    raise ValueError("\u274c Missing BrowserStack credentials!")

BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Test Configuration
TEST_URL = "https://eatanceapp.com/"
SCREENSHOT_DIR = os.path.abspath("screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

devices = [
    {"device": "Samsung Galaxy S22", "os_version": "12.0", "browser": "Chrome"},
    {"device": "iPhone 14", "os_version": "16.0", "browser": "Safari"}
]

BASELINE_DEVICE = "Samsung Galaxy S22"
baseline_screenshot = None
results = []

def get_driver(device_info):
    options = webdriver.ChromeOptions()
    options.set_capability('browserstack.user', BROWSERSTACK_USERNAME)
    options.set_capability('browserstack.key', BROWSERSTACK_ACCESS_KEY)
    options.set_capability('device', device_info["device"])
    options.set_capability('os_version', device_info["os_version"])
    options.set_capability('browser', device_info["browser"])
    options.set_capability('real_mobile', 'true')
    return webdriver.Remote(command_executor=BROWSERSTACK_URL, options=options)

def capture_full_page_screenshot(driver, name, hidden_elements=None, is_mobile=False):
    """Scroll and capture full-page screenshots without missing content or leaving whitespace."""
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}_full.png")
    
    pixel_ratio = 1
    if is_mobile:
        pixel_ratio = driver.execute_script("return window.devicePixelRatio")
    
    # Get page dimensions
    full_width = int(driver.execute_script("return document.body.offsetWidth") * pixel_ratio)
    total_height = int(driver.execute_script("return document.body.parentNode.scrollHeight") * pixel_ratio)
    
    # Get viewport dimensions
    viewport_width = int(driver.execute_script("return document.body.clientWidth") * pixel_ratio)
    viewport_height = int(driver.execute_script("return window.innerHeight") * pixel_ratio)
    
    # Hide specified elements
    if hidden_elements:
        for element_xpath in hidden_elements:
            elements = driver.find_elements(By.XPATH, element_xpath)
            for element in elements:
                driver.execute_script("arguments[0].style.visibility='hidden'", element)
    
    time.sleep(2)  # Let everything load

    part_images = []
    y_offset = 0
    scroll_position = 0
    part = 0
    overlap_height = 2  # Set overlap height (adjust based on the page content)
    
    # Height of the bottom navigation bar (adjust as needed)
    nav_bar_height = 100  # Change this value based on your device

    while scroll_position < total_height:
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(2)  # Allow page to load

        part_path = os.path.join(SCREENSHOT_DIR, f"{name}_part{part}.png")
        driver.save_screenshot(part_path)
        part_img = Image.open(part_path).convert("RGB")

        if part == 0:
            fixed_width = part_img.width  # Store the first part's width

        # Resize all images to the same width
        if part_img.width != fixed_width:
            part_img = part_img.resize((fixed_width, part_img.height), Image.Resampling.LANCZOS)

        # Crop the bottom navigation bar from the last part
        if scroll_position + viewport_height >= total_height:
            part_img = part_img.crop((0, 0, part_img.width, part_img.height - nav_bar_height))

        part_images.append((part_img, y_offset))
        y_offset += part_img.height - overlap_height  # Ensure the overlap by reducing y_offset
        scroll_position += viewport_height - overlap_height  # Scroll by less to create overlap
        part += 1

        # Check if we've reached the bottom and stop scrolling
        if scroll_position >= total_height:
            break
        
        # Calculate the total height to confirm alignment
    total_height = sum([img.height for img, _ in part_images])
    print(f"Calculated total height: {total_height}")

    # Create stitched image
    stitched_image = Image.new('RGB', (fixed_width, total_height))
    current_y = 0

    # Paste all the images at their respective y_offsets
    for img, y in part_images:
        print(f"Pasting part at Y position: {current_y}")
        if current_y + img.height > total_height:
            img = img.crop((0, 0, fixed_width, total_height - current_y))
        stitched_image.paste(img, (0, current_y))
        current_y += img.height

    stitched_image.save(screenshot_path)
    print(f"✅ Full-page screenshot saved: {screenshot_path}")
    return screenshot_path


def compare_images(baseline_path, test_path, output_path):
    baseline = Image.open(baseline_path).convert("RGB")
    test = Image.open(test_path).convert("RGB").resize(baseline.size)
    
    diff = ImageChops.difference(baseline, test)
    bbox = diff.getbbox()
    if bbox:
        baseline_cv = np.array(baseline)
        test_cv = np.array(test)
        diff_gray = cv2.absdiff(baseline_cv, test_cv)
        diff_gray = cv2.cvtColor(diff_gray, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(diff_gray, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(test_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        diff_path = os.path.join(output_path, "compared.png")
        cv2.imwrite(diff_path, test_cv)
        return True, diff_path
    return False, baseline_path

def run_tests():
    global baseline_screenshot
    for device in devices:
        driver = get_driver(device)
        driver.get(TEST_URL)
        time.sleep(5)
        
        try:
            screenshot_path = capture_full_page_screenshot(driver, device["device"])
        except Exception as e:
            print(f"\u274c Screenshot capture failed: {e}")
            driver.quit()
            continue
        
        if device["device"] == BASELINE_DEVICE:
            baseline_screenshot = screenshot_path
        else:
            has_diff, diff_path = compare_images(baseline_screenshot, screenshot_path, SCREENSHOT_DIR)
            border_color = "red" if has_diff else "green"
            status_text = "Differences Found" if has_diff else "No Differences"
            results.append({
                "device": device["device"],
                "baseline_image": baseline_screenshot,
                "test_image": screenshot_path,
                "diff_image": diff_path,
                "border": border_color,
                "status": status_text
            })
        driver.quit()
    generate_html_report()


def generate_html_report():
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