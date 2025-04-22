import subprocess
import time
import pyautogui
import os
import csv
from datetime import datetime
import pygetwindow as gw
import json
from openpyxl import Workbook

# Path to Postman executable and collection
postman_exe = r"C:\\Users\\Evince\\AppData\\Local\\Postman\\Postman.exe"
collection_file = r"C:\\Clymb_Automation\\Magento_API\\Magento_API_Collection.postman_collection.json"
screenshot_dir = "postman_desktop_screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Excel log file path
excel_log_file = "api_screenshot_log.xlsx"

# Initialize Excel workbook and sheet
def init_excel_log():
    if not os.path.exists(excel_log_file):
        wb = Workbook()
        ws = wb.active
        ws.title = "API Logs"
        ws.append(["API URL", "Screenshot Path", "Timestamp"])  # Headers
        wb.save(excel_log_file)

def focus_postman():
    try:
        windows = gw.getWindowsWithTitle("Postman")
        if windows:
            postman_window = windows[0]
            postman_window.restore()
            postman_window.maximize()
            postman_window.activate()
            time.sleep(1)
            
            # Ensure Postman is in focus using Alt+Tab trick
            pyautogui.hotkey('alt', 'tab')
            time.sleep(1)
            return True
        else:
            print("⚠️ Postman window not found.")
    except Exception as e:
        print(f"Error focusing on Postman window: {e}")
    return False

# Capture screenshot
def capture_screenshot(request_url):
    if focus_postman():
        safe_url = request_url.replace("https://", "").replace("/", "_")
        screenshot_path = os.path.join(
            screenshot_dir,
            f"screenshot_{safe_url}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        pyautogui.screenshot(screenshot_path)
        print(f"📸 Screenshot saved: {screenshot_path}")
        return screenshot_path
    else:
        print("❌ Could not focus Postman window.")
        return None

# Log to Excel
def log_to_excel(api_url, screenshot_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "API Logs"
    ws.append([api_url, screenshot_path, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    wb.save(excel_log_file)

# Run Newman
def run_newman_collection(collection_file):
    newman_command = f"newman run \"{collection_file}\" --reporters json --reporter-json-export newman_report.json"
    subprocess.run(newman_command, shell=True)

# ✅ Correct version of process_newman_report
def process_newman_report(report_file):
    try:
        with open(report_file, 'r') as f:
            report_data = json.load(f)

        for item in report_data.get("run", {}).get("executions", []):
            request_data = item.get("request", {}).get("url", {})
            protocol = request_data.get("protocol", "")
            host = ".".join(request_data.get("host", []))
            path = "/".join(request_data.get("path", []))

            if protocol and host and path:
                request_url = f"{protocol}://{host}/{path}"
            else:
                request_url = "URL not found"

            print(f"Request URL: {request_url}")
            # Focus Postman window and send request
            if focus_postman():
                # Step 1: Focus on the URL input field in Postman (you may need to adjust the coordinates)
                url_input_position = (400, 200)  # Coordinates of the URL input field in Postman
                pyautogui.click(url_input_position)
                time.sleep(1)  # Allow time for the field to be focused
                
                # Step 2: Clear the URL field (CTRL+A, Delete)
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(0.5)
                pyautogui.press('delete')
                time.sleep(0.5)

                # Step 3: Type the new URL into the field
                pyautogui.write(request_url)
                time.sleep(1)  # Wait for the URL to be fully typed

                # Step 4: Click on the "Send" button (coordinates)
                send_button_position = (1230, 160)  # Adjust this based on your screen resolution
                pyautogui.click(send_button_position)
                time.sleep(3)  # Wait for the response

                # Step 5: Capture screenshot after receiving the response
                screenshot_path = capture_screenshot(request_url)
                if screenshot_path:
                    log_to_excel(request_url, screenshot_path)

    except FileNotFoundError:
        print(f"Report file {report_file} not found.")

# Main execution
if __name__ == "__main__":
    init_excel_log()  # Initialize Excel log if not already present
    
    print("🚀 Launching Postman...")
    subprocess.Popen(postman_exe)
    time.sleep(10)

    print("🛠️ Running Postman collection...")
    run_newman_collection(collection_file)

    print("🔍 Processing Newman report...")
    process_newman_report("newman_report.json")

    print("✅ Finished capturing screenshots and logging URLs.")
