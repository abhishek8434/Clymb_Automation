from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import time
import os
import json
from dotenv import load_dotenv
from PIL import Image, ImageChops
from selenium.webdriver.chrome.options import Options
from datetime import datetime
current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

load_dotenv()

USERNAME = os.getenv("BROWSERSTACK_USERNAME")    
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")  

if not USERNAME or not ACCESS_KEY:
    raise ValueError("❌ BROWSERSTACK_USERNAME or BROWSERSTACK_ACCESS_KEY is missing from environment variables!")

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

DEVICES = [
    {"device": "Samsung Galaxy S22", "os_version": "12.0", "browser": "Chrome"},
    {"device": "iPhone 12", "os_version": "14.0", "browser": "Safari"},
    {"device": "iPhone 13", "os_version": "15.0", "browser": "Safari"},
    {"device": "iPhone 14", "os_version": "16.0", "browser": "Safari"},
    {"device": "iPhone 15", "os_version": "17.0", "browser": "Safari"},
    {"device": "Samsung Galaxy S21", "os_version": "11.0", "browser": "Chrome"},
    {"device": "Samsung Galaxy S23", "os_version": "13.0", "browser": "Chrome"},
]

TEST_URL = "https://clymbstudent.evdpl.com/account/login"
SCREENSHOT_DIR = os.path.abspath("screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
BASELINE_DEVICE = "Samsung Galaxy S22"
baseline_image = None
results = []

def get_driver(config):
    capabilities = {
        "browserstack.user": USERNAME,
        "browserstack.key": ACCESS_KEY,
        **config
    }
    options = Options()
    for key, value in capabilities.items():
        options.set_capability(key, value)
    try:
        return webdriver.Remote(command_executor=BROWSERSTACK_URL, options=options)
    except Exception as e:
        print(f"❌ Failed to create WebDriver for {config}: {e}")
        return None

def take_screenshot(driver: WebDriver, name: str):
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path if os.path.exists(screenshot_path) else None

def compare_screenshots(image1_path, image2_path, device):
    if not os.path.exists(image1_path) or not os.path.exists(image2_path):
        print(f"❌ Missing images for comparison: {image1_path}, {image2_path}")
        return
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    diff = ImageChops.difference(img1, img2)
    diff_path = os.path.join(SCREENSHOT_DIR, f"diff_{device}.png")
    if diff.getbbox():
        diff.save(diff_path)
        result = {"device": device, "status": "⚠️ Difference Detected", "diff_image": diff_path}
        print(f"⚠️ Difference detected for {device}")
    else:
        result = {"device": device, "status": "✅ No Difference", "diff_image": None}
        print(f"✅ No Difference for {device}")
    results.append(result)
    
def generate_html_report():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>UI Test Report</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; }
            table { width: 100%; border-collapse: collapse; background: white; }
            h2 {text-align: center;}
            th, td { padding: 10px; border: 1px solid black; text-align: center; font-weight: bold;}
            .pass { border: 3px solid green; }
            .fail { border: 3px solid red; }
            img { max-width: 200px; display: block; margin: 0 auto; }
            header { background-color: #ffffff; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
            footer { text-align: center; padding: 10px; background: #f1f1f1; }
        </style>
    </head>
    <body>
        <header>
            <h1>Site UI Comparison Report</h1>
        </header>
        <h2>UI Test Report</h2>
        <table>
            <tr>
                <th>Device</th>
                <th>Baseline (S22)</th>
                <th>Comparison</th>
                <th>Difference</th>
            </tr>
    """
    for result in results:
        status_class = "fail" if result["diff_image"] else "pass"
        diff_img = f"<img src='{result['diff_image']}' width='200'>" if result["diff_image"] else "No Difference"
        baseline_img_path = os.path.join(SCREENSHOT_DIR, f"{BASELINE_DEVICE}.png")
        comparison_img_path = os.path.join(SCREENSHOT_DIR, f"{result['device']}.png")
        html_content += f"""
            <tr>
                <td>{result['device']}</td>
                <td><img src='file:///{baseline_img_path}' width='200'></td>
                <td><img src='file:///{comparison_img_path}' width='200' class='{status_class}'></td>
                <td>{diff_img}</td>
            </tr>
        """
    html_content += f"</table><footer>Report generated on {current_date_time}</footer></body></html>"

    report_path = os.path.join(SCREENSHOT_DIR, "ui_test_report.html")
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(html_content)
    print(f"📄 Test report generated: {report_path}")

def run_tests():
    global baseline_image
    for device in DEVICES:
        device_name = device["device"]
        print(f"🚀 Testing on: {device_name}")
        driver = get_driver(device)
        if not driver:
            continue
        driver.get(TEST_URL)
        time.sleep(5)
        screenshot_path = take_screenshot(driver, device_name)
        if not screenshot_path:
            print(f"❌ Screenshot failed for {device_name}")
            continue
        if device_name == BASELINE_DEVICE:
            baseline_image = screenshot_path
        else:
            compare_screenshots(baseline_image, screenshot_path, device_name)
        driver.quit()
    generate_html_report()

if __name__ == "__main__":
    run_tests()