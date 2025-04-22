import os
import time
import cv2
import numpy as np
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions

# --- CONFIGURATIONS ---
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")    
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")  

if not BROWSERSTACK_USERNAME or not BROWSERSTACK_ACCESS_KEY:
    raise ValueError("❌ Missing BrowserStack credentials!")

BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

SCREENSHOT_DIR = os.path.abspath("screenshots")
BASELINE_DEVICE = "Samsung Galaxy S22"
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
TEST_URL = "https://new.evincedev.com/shopify-development"
# Devices to test on
DEVICES = [
    {"device": "Samsung Galaxy S22", "os_version": "12.0", "browser": "chrome"},
    {"device": "iPhone 14", "os_version": "16", "browser": "safari"},
    # Add more devices if needed
]

results = []
baseline_screenshot = ""

# --- DRIVER SETUP (using options with capabilities) ---
def get_driver(device_config):
    if device_config["browser"] == "chrome":
        options = ChromeOptions()
    elif device_config["browser"] == "safari":
        options = SafariOptions()
    else:
        raise ValueError(f"Unsupported browser: {device_config['browser']}")

    # Set BrowserStack options and capabilities
    options.set_capability("bstack:options", {
        "deviceName": device_config["device"],
        "realMobile": "true",
        "osVersion": device_config["os_version"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY,
        "buildName": "UI Screenshot Testing",
        "sessionName": f"UI Visual Test on {device_config['device']}",
    })

    options.set_capability("browserName", device_config["browser"])

    # Initialize the driver with the configured options
    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    return driver

# --- HANDLE COOKIE POPUP (MODIFY FOR YOUR SITE) ---
def handle_cookie_consent(driver):
    try:
        cookiepop = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='i-accept']"))
            
        )
        print(f"\n🍪 Cookie popup is visible")
        cookiepop.click()
       
        print(f"\n🍪 Clicked on Cookie popup")
    except:
        print(f"\n🍪 Cookie popup is not visible ")
        pass  # Ignore if no popup

# --- SCROLLING AND TAKING SCREENSHOT ---
def take_full_page_screenshot(driver, device_name):
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        page_height = driver.execute_script("return document.body.scrollHeight")
        viewport_height = driver.execute_script("return window.innerHeight")
        scroll_position = 0
        screenshots = []

        while scroll_position < page_height:
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            time.sleep(2)

            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{device_name}_{scroll_position}.png")
            driver.save_screenshot(screenshot_path)
            screenshots.append(screenshot_path)

            scroll_position += viewport_height
            if scroll_position >= page_height:
                break

        full_page_screenshot = stitch_screenshots(screenshots, device_name)
        return full_page_screenshot
    except Exception as e:
        print(f"❌ Failed to take full-page screenshot for {device_name}: {e}")
        return None
    
# --- STITCHING MULTIPLE SCREENSHOTS ---
def stitch_screenshots(screenshot_paths, device_name):
    images = [Image.open(path) for path in screenshot_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    total_height = sum(heights)

    # Create a new image with a height that is the sum of all screenshots
    full_image = Image.new('RGB', (total_width, total_height))

    current_height = 0
    for img in images:
        full_image.paste(img, (0, current_height))
        current_height += img.height

    stitched_path = os.path.join(SCREENSHOT_DIR, f"{device_name}_fullpage.png")
    full_image.save(stitched_path)
    print(f"✅ Full page screenshot saved at: {stitched_path}")
    return stitched_path

# --- COMPARE IMAGES ---
def compare_images(baseline_path, test_path, output_path, device_name):
    baseline = Image.open(baseline_path).convert("RGB")
    test = Image.open(test_path).convert("RGB")
    test = test.resize(baseline.size)

    diff = ImageChops.difference(baseline, test)
    bbox = diff.getbbox()

    diff_description = "No visual differences detected."
    compared_path = test_path

    if bbox:
        baseline_cv = cv2.cvtColor(np.array(baseline), cv2.COLOR_RGB2BGR)
        test_cv = cv2.cvtColor(np.array(test), cv2.COLOR_RGB2BGR)

        diff_gray = cv2.cvtColor(cv2.absdiff(baseline_cv, test_cv), cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(diff_gray, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        regions = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(test_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)
            page_section = "top" if y < baseline.height / 3 else "middle" if y < 2 * baseline.height / 3 else "bottom"
            regions.append(f"Region at {page_section} section (coordinates: {x},{y} size: {w}x{h})")

        if regions:
            if len(regions) > 3:
                section_counts = {"top": 0, "middle": 0, "bottom": 0}
                for r in regions:
                    if "top section" in r:
                        section_counts["top"] += 1
                    elif "middle section" in r:
                        section_counts["middle"] += 1
                    elif "bottom section" in r:
                        section_counts["bottom"] += 1

                sections = [s for s, count in section_counts.items() if count > 0]
                diff_description = f"Found {len(regions)} areas with visual differences in the " + " and ".join(sections) + " sections."
            else:
                diff_description = "Found visual differences in: " + "; ".join(regions)

        compared_path = os.path.join(output_path, f"{device_name}_compared.png")
        cv2.imwrite(compared_path, test_cv)

        return True, compared_path, diff_description

    return False, test_path, diff_description

# --- MAIN TEST RUNNER ---
def run_tests():
    global baseline_screenshot

    for device in DEVICES:
        device_name = device["device"]
        print(f"\n🔍 Testing on: {device_name}")

        try:
            driver = get_driver(device)
            driver.get(TEST_URL)
            print(f"🌐 Opened: {TEST_URL}")

            handle_cookie_consent(driver)
            screenshot_path = take_full_page_screenshot(driver, device_name)

            if not screenshot_path:
                driver.quit()
                continue

        except Exception as e:
            print(f"❌ Test failed for {device_name}: {str(e)}")
            continue
        finally:
            try:
                driver.quit()
            except:
                pass

        if device_name == BASELINE_DEVICE:
            baseline_screenshot = screenshot_path
            results.append({
                "device": device_name,
                "os_version": device["os_version"],
                "browser": device["browser"],
                "screenshot": screenshot_path,
                "is_baseline": True,
                "differences": "Baseline for comparison",
                "status": "Baseline"
            })
        else:
            has_diff, compared_path, diff_description = compare_images(
                baseline_screenshot, screenshot_path, SCREENSHOT_DIR, device_name
            )
            status = "Differences Found" if has_diff else "No Differences"
            results.append({
                "device": device_name,
                "os_version": device["os_version"],
                "browser": device["browser"],
                "screenshot": compared_path,
                "is_baseline": False,  # ✅ FIXED
                "differences": diff_description,
                "status": status
            })

    generate_html_report()

# --- HTML REPORT ---
def generate_html_report():
    report_path = os.path.join(SCREENSHOT_DIR, "ui_shopify_report.html")
    if not results:
        print("⚠️ No results to generate report.")
        return

    html = """
    <html><head><title>UI Report</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; padding: 20px; }
        table { width: 100%; border-collapse: collapse; }
        td, th { border: 1px solid #ccc; padding: 10px; text-align: center; }
        img { width: 100%; object-fit: contain; }
        .baseline { background-color: #e8f4ff; }
        .diff { background-color: #fff0f0; }
        .no-diff { background-color: #f0fff0; }
    </style></head><body>
    <h1>UI Visual Test Report</h1>
    <table><tr>"""

    for res in results:
        cls = "baseline" if res["is_baseline"] else "diff" if res["status"] == "Differences Found" else "no-diff"
        html += f"<th class='{cls}'>{res['device']}<br>({res['browser']})</th>"
    html += "</tr><tr>"

    for res in results:
        html += f"<td><img src='{os.path.basename(res['screenshot'])}'><br>{res['status']}</td>"
    html += "</tr><tr>"

    for res in results:
        html += f"<td>{res['differences']}</td>"
    html += "</tr></table></body></html>"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Report saved at: {report_path}")

# --- MAIN ---
if __name__ == "__main__":
    run_tests()
