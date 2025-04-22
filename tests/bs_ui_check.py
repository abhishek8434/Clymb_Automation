from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import time
import os
import json
from dotenv import load_dotenv
from PIL import Image, ImageChops
from selenium.webdriver.chrome.options import Options

load_dotenv()

# Get login details from environment variables
USERNAME = os.getenv("BROWSERSTACK_USERNAME")    
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")  

# Validate credentials
if not USERNAME or not ACCESS_KEY:
    raise ValueError("❌ BROWSERSTACK_USERNAME or BROWSERSTACK_ACCESS_KEY is missing from environment variables!")

# BrowserStack URL
BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# List of devices to test
DEVICES = [
    {"os": "Windows", "os_version": "10", "browser": "Chrome", "browser_version": "latest"},
    {"os": "Windows", "os_version": "10", "browser": "Edge", "browser_version": "latest"},
    {"os": "OS X", "os_version": "Monterey", "browser": "Safari", "browser_version": "latest"},
    {"device": "Samsung Galaxy S22", "os_version": "12.0", "browser": "Chrome"},
    # {"device": "iPhone 14", "os_version": "16.0", "browser": "Safari"},
    # {"device": "iPhone 12", "os_version": "14.0", "browser": "Safari"},
    # {"device": "iPhone 13", "os_version": "15.0", "browser": "Safari"},
    # {"device": "iPhone 15", "os_version": "17.0", "browser": "Safari"}
]

# URL to test
TEST_URL = "https://clymbstudent.evdpl.com/account/login"

# Screenshot directory
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Results storage
results = []

# Create driver instance
def get_driver(config):
    """Initialize WebDriver for BrowserStack."""
    capabilities = {
        "browserstack.user": USERNAME,
        "browserstack.key": ACCESS_KEY,
        **config  # Merge device-specific capabilities
    }
    
    options = Options()
    
    # Set capabilities for BrowserStack
    for key, value in capabilities.items():
        options.set_capability(key, value)

    try:
        driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            options=options  # Correct way to pass capabilities
        )
        return driver
    except Exception as e:
        print(f"❌ Failed to create WebDriver for {config}: {e}")
        return None

# Take screenshot
def take_screenshot(driver: WebDriver, name: str):
    """Capture a screenshot and save it."""
    screenshot_path = f"{SCREENSHOT_DIR}/{name}.png"
    driver.save_screenshot(screenshot_path)
    return screenshot_path

# Compare screenshots
def compare_screenshots(image1_path, image2_path, index, device):
    """Compare two screenshots and log differences."""
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    diff = ImageChops.difference(img1, img2)
    if diff.getbbox():
        diff_path = f"{SCREENSHOT_DIR}/diff_device_{index}.png"
        diff.save(diff_path)

        result = {
            "device": device,
            "status": "⚠️ UI Difference Detected",
            "diff_screenshot": diff_path
        }
        print(f"⚠️ UI Difference detected! Difference saved at {diff_path}")
    else:
        result = {
            "device": device,
            "status": "✅ No UI Difference",
            "diff_screenshot": None
        }
        print(f"✅ No UI difference detected.")
    
    results.append(result)

# Run test on multiple devices
def run_tests():
    """Run UI tests across multiple devices."""
    baseline_image = None
    for index, device in enumerate(DEVICES):
        print(f"🚀 Testing on: {device}")

        driver = get_driver(device)
        if not driver:
            continue  # Skip this device if WebDriver fails to initialize
        
        driver.get(TEST_URL)
        time.sleep(5)  # Allow page to load

        screenshot_path = take_screenshot(driver, f"device_{index}")

        if baseline_image:
            compare_screenshots(baseline_image, screenshot_path, index, device)
        else:
            baseline_image = screenshot_path  # First image as baseline

        print(f"✅ Test completed on {device}")
        driver.quit()

    # Save report
    with open("ui_test_report.json", "w") as report_file:
        json.dump(results, report_file, indent=4)

    print("📊 Test report generated: ui_test_report.json")

if __name__ == "__main__":
    run_tests()
