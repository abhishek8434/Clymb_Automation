import os
import time
import cv2
import numpy as np
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()
import logging

BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")    
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")  



if not BROWSERSTACK_USERNAME or not BROWSERSTACK_ACCESS_KEY:
    raise ValueError("❌ Missing BrowserStack credentials!")

BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"


# Test Configuration
TEST_URL = "https://new.evincedev.com/shopify-development"
SCREENSHOT_DIR = os.path.abspath("screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

DEVICES = [
    {"device": "Samsung Galaxy S22", "os_version": "12.0", "browser": "Chrome"},
    {"device": "Samsung Galaxy S23", "os_version": "13.0", "browser": "Chrome"},
    # {"device": "Samsung Galaxy Z Fold 6", "os_version": "14.0", "browser": "Chrome"},
    # {"device": "Google Pixel 6 Pro", "os_version": "13.0", "browser": "Chrome"},
    {"device": "iPhone 14", "os_version": "16.0", "browser": "Safari"},
    {"device": "iPhone 12", "os_version": "14.0", "browser": "Safari"},
    {"device": "iPhone 13", "os_version": "15.0", "browser": "Safari"},
    {"device": "iPhone 14", "os_version": "16.0", "browser": "Safari"},
    {"device": "iPhone 15", "os_version": "17.0", "browser": "Safari"},
]

BASELINE_DEVICE = "Samsung Galaxy S22"
baseline_screenshot = None
results = []

def get_driver(device_info):
    print(f"🔍 Debug: Device info received -> {device_info} ({type(device_info)})")  # Debugging line

    # Ensure we are extracting the correct device name
    device_name = device_info.get('device', 'Samsung Galaxy S22')  # Default if not found

    options = webdriver.ChromeOptions()
    options.set_capability('browserstack.user', BROWSERSTACK_USERNAME)
    options.set_capability('browserstack.key', BROWSERSTACK_ACCESS_KEY)
    options.set_capability('device', device_name)  # Now it's correctly a string
    options.set_capability('os_version', device_info.get('os_version', '12.0'))
    options.set_capability('browser', device_info.get('browser', 'Chrome'))
    options.set_capability('real_mobile', 'true')

    return webdriver.Remote(command_executor=BROWSERSTACK_URL, options=options)

def crop_browser_ui(image_path, driver):
    """Dynamically crop the browser UI."""
    img = Image.open(image_path)
    width, height = img.size
    
    # Detect Navbar height dynamically
    navbar_height = driver.execute_script("""
        let nav = document.querySelector('.fixed-header, .sticky, .back-to-top');
        return nav ? nav.offsetHeight : 0;
    """)

    footer_height = 50  # Approximate footer size if present
    if height > navbar_height + footer_height:
        img = img.crop((0, navbar_height, width, height - footer_height))

    img.save(image_path)
    print(f"📸 Cropped browser UI from {image_path}")

def capture_full_page_screenshot(driver, name, max_scroll_height=None):
    """Capture a full-page screenshot by scrolling and stitching."""
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    scroll_positions = list(range(0, total_height, viewport_height))
    
    images = []
    
    for i, pos in enumerate(scroll_positions):
        driver.execute_script(f"window.scrollTo(0, {pos});")
        time.sleep(1)
        path = os.path.join(SCREENSHOT_DIR, f"{name}_part_{i}.png")
        driver.save_screenshot(path)
        images.append(Image.open(path))

    # Stitch vertically
    full_image = Image.new("RGB", (images[0].width, sum(img.height for img in images)))
    current_y = 0
    for img in images:
        full_image.paste(img, (0, current_y))
        current_y += img.height

    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}_fullpage.png")
    full_image.save(screenshot_path)

    # Clean up temp parts
    for i in range(len(images)):
        os.remove(os.path.join(SCREENSHOT_DIR, f"{name}_part_{i}.png"))

    return screenshot_path


def compare_images(baseline_path, test_path, output_path):
    """Compares two images and highlights differences."""
    baseline = Image.open(baseline_path).convert("RGB")
    test = Image.open(test_path).convert("RGB")

    # Resize test image to match baseline
    test = test.resize(baseline.size)

    diff = ImageChops.difference(baseline, test)
    bbox = diff.getbbox()

    if bbox:
        baseline_cv = cv2.cvtColor(np.array(baseline), cv2.COLOR_RGB2BGR)
        test_cv = cv2.cvtColor(np.array(test), cv2.COLOR_RGB2BGR)

        diff_gray = cv2.cvtColor(cv2.absdiff(baseline_cv, test_cv), cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(diff_gray, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(test_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)

        compared_path = os.path.join(output_path, "compared.png")
        cv2.imwrite(compared_path, test_cv)

        return True, compared_path

    return False, baseline_path

def run_tests():
    """Run UI tests on all devices and store results."""
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
            continue

        if device_name == BASELINE_DEVICE:
            baseline_screenshot = screenshot_path
            print(f"📌 Baseline screenshot set for {BASELINE_DEVICE}")
        else:
            has_diff, diff_path = compare_images(baseline_screenshot, screenshot_path, SCREENSHOT_DIR)
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
    """Generate an HTML report with results."""
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
