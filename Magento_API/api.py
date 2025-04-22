import time
import json
import os
import pyautogui
import subprocess
import pandas as pd
from datetime import datetime
import pygetwindow as gw
import pygetwindow as gw
import win32gui
import win32con
import time


# === CONFIGURATION ===
newman_cmd = r"C:\\Users\\Evince\\AppData\\Roaming\\npm\\newman.cmd"
collection_path = r"C:\\Clymb_Automation\\Magento_API\\Report\\Replacebase_API_Collection.json"  # <== Replace this with your actual collection path
report_json_path = r"C:\\Clymb_Automation\\Magento_API\\Report\\results.json"
output_file = "API_Test_Results.xlsx"
screenshot_dir = "postman_screenshots"

# Create folders if not exist
os.makedirs(os.path.dirname(report_json_path), exist_ok=True)
os.makedirs(screenshot_dir, exist_ok=True)

# === RUN POSTMAN COLLECTION ===
def run_newman_collection():
    try:
        result = subprocess.run(
            [newman_cmd, "run", collection_path, "-r", "json", "--reporter-json-export", report_json_path],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print("✅ Newman run completed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Newman run failed: {e}")
        return False
    return True

# === CAPTURE SCREENSHOT ===
def capture_screenshot(api_index):
    time.sleep(2)

    # Find the Postman app window only (exclude browsers)
    postman_windows = [
        w for w in gw.getAllTitles() if 'Postman' in w and 'Google Chrome' not in w and 'Edge' not in w
    ]

    if not postman_windows:
        print("❌ Postman desktop app not found.")
        return None

    # Use exact window title (usually just "Postman")
    for title in postman_windows:
        try:
            win = gw.getWindowsWithTitle(title)[0]
            if win:
                hwnd = win._hWnd

                if win.isMinimized:
                    win.restore()

                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
                time.sleep(2)

                # Screenshot region of Postman window
                left, top, width, height = win.left, win.top, win.width, win.height
                screenshot = pyautogui.screenshot(region=(left, top, width, height))

                screenshot_path = os.path.join(screenshot_dir, f"response_{api_index + 1}.png")
                screenshot.save(screenshot_path)
                print(f"✅ Screenshot saved: {screenshot_path}")
                return screenshot_path

        except Exception as e:
            print(f"⚠️ Failed to activate window '{title}': {e}")

    print("❌ No valid Postman window could be activated.")
    return None

# === PARSE REPORT JSON + SAVE TO EXCEL ===
def process_results_to_excel(results_json):
    # Load the Newman results
    with open(results_json, 'r') as f:
        data = json.load(f)

    results = []

    for idx, execution in enumerate(data['run']['executions']):
        # Handle both raw and string URL formats
        url_field = execution['request']['url']
        if isinstance(url_field, dict):
            endpoint = url_field.get('raw') or '/'.join(url_field.get('path', []))
        else:
            endpoint = url_field

        status_code = execution['response']['status']
        screenshot_path = capture_screenshot(idx)

        results.append({
            "S.No": idx + 1,
            "Endpoint": endpoint,
            "Status Code": status_code,
            "Screenshot Path": screenshot_path,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # Save results into an Excel file
    df = pd.DataFrame(results)
    df.to_excel(output_file, index=False)
    print(f"✅ Results saved to {output_file}")
    
# === MAIN ===
if __name__ == "__main__":
    if run_newman_collection():
        process_results_to_excel(report_json_path)
