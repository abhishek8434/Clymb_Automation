import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageChops
import difflib
from datetime import datetime
from dotenv import load_dotenv
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions

load_dotenv()

BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

url_to_test = "https://eatanceapp.com/"
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)
report_path = "full_content_comparison_report.html"

devices = [
    {'device': 'Samsung Galaxy S22', 'os_version': '12.0', 'name': 'S22'},
    {'device': 'iPhone 14', 'os_version': '16', 'name': 'iPhone14'}
]

def fullpage_screenshot(driver, save_path, crop_top=0):
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    page_width = driver.execute_script("return document.documentElement.scrollWidth")

    stitched_image = Image.new('RGB', (page_width, total_height))
    scroll = 0
    index = 0
    stitched_y = 0

    while scroll < total_height:
        driver.execute_script(f"window.scrollTo(0, {scroll});")
        time.sleep(0.8)

        tmp_path = f"part_{index}.png"
        driver.save_screenshot(tmp_path)
        screenshot = Image.open(tmp_path)

        cropped = screenshot.crop((0, crop_top, page_width, viewport_height))
        stitched_image.paste(cropped, (0, stitched_y))

        os.remove(tmp_path)
        stitched_y += (viewport_height - crop_top)
        scroll += viewport_height
        index += 1

    if stitched_y > total_height:
        stitched_image = stitched_image.crop((0, 0, page_width, total_height))

    stitched_image.save(save_path)

def run_test_and_capture(device):
    print(f"Testing on {device['name']}...")
    
    caps = {
        'browserName': 'Chrome',
        'device': device['device'],
        'realMobile': 'true',
        'os_version': device['os_version'],
        'name': f"{device['name']} Content Test",
        'browserstack.debug': True,
        'browserstack.console': 'errors',
        'browserstack.networkLogs': True,
    }

    options = ChromeOptions()
    for key, value in caps.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    driver.get(url_to_test)

    # MJSONWP-compatible wait:
    driver.execute_script("browserstack_executor: {\"action\": \"setTimeout\", \"arguments\": {\"type\": \"implicit\", \"ms\": 10000}}")

    crop_top = 80 if "iPhone" in device['device'] else 0

    screenshot_path = os.path.join(screenshot_dir, f"{device['name']}_full.png")
    fullpage_screenshot(driver, screenshot_path, crop_top=crop_top)

    text = driver.find_element(By.TAG_NAME, "body").text.strip()
    normalized_text = ' '.join(text.split())

    driver.quit()
    return screenshot_path, normalized_text

def compare_images(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)

    if diff.getbbox():
        diff_path = os.path.join(screenshot_dir, "visual_diff.png")
        diff.save(diff_path)
        return True, diff_path
    return False, ""

def compare_text(text1, text2):
    differ = difflib.HtmlDiff()
    return differ.make_table(text1.split(), text2.split(), context=True, numlines=2)

def generate_final_report(screenshot_data, visual_diff_found, visual_diff_path, text_diff_html):
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Unified Content Comparison Report</title>")
        f.write("<style>body{font-family:sans-serif;} table{border-collapse:collapse;} td{padding:5px;}</style>")
        f.write("</head><body>")
        f.write(f"<h1>Unified Content Comparison Report</h1>")
        f.write(f"<p><strong>Tested URL:</strong> {url_to_test}</p>")
        f.write(f"<p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")

        f.write("<h2>📷 Screenshots</h2>")
        f.write("<table><tr>")
        for data in screenshot_data:
            f.write(f"<td style='vertical-align: top;'><strong>{data['device_name']}</strong><br><img src='{data['screenshot']}' width='300'></td>")
        f.write("</tr></table>")

        f.write("<h2>🖼️ Visual Comparison</h2>")
        if visual_diff_found:
            f.write("<p style='color:red;'>❌ Visual differences detected</p>")
            f.write(f"<img src='{visual_diff_path}' width='600'>")
        else:
            f.write("<p style='color:green;'>✅ No visual differences detected</p>")

        f.write("<h2>📝 Text Comparison</h2>")
        f.write(text_diff_html)

        f.write("</body></html>")

    print(f"✅ Final report generated: {report_path}")

if __name__ == "__main__":
    print("Running cross-device test...")

    screenshot_data = []
    text_results = []

    for device in devices:
        ss, txt = run_test_and_capture(device)
        screenshot_data.append({'device_name': device['name'], 'screenshot': ss})
        text_results.append(txt)

    print("Comparing screenshots...")
    visual_diff_found, visual_diff_path = compare_images(
        screenshot_data[0]['screenshot'], screenshot_data[1]['screenshot']
    )

    print("Comparing text content...")
    text_diff_html = compare_text(text_results[0], text_results[1])

    print("Generating report...")
    generate_final_report(screenshot_data, visual_diff_found, visual_diff_path, text_diff_html)
