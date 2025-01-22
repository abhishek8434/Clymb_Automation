import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageDraw, ImageFont
from skimage.metrics import structural_similarity as ssim
from contextlib import contextmanager
import numpy as np
from datetime import datetime
import base64

ASSETS_DIR = "assets"
REPORTS_DIR = "reports"
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

@contextmanager
def driver():
    """Initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        yield driver
    finally:
        driver.quit()


def get_current_date():
    """Returns the current date in a readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def convert_image_to_base64(image_path):
    """Convert image to Base64 encoded string."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


def capture_screenshot(url, save_path, driver, login_required=False, username=None, password=None):
    """Capture a screenshot of a given URL."""
    driver.get(url)

    if login_required:
        print("Logging in...")
        try:
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@aria-label='LOGIN']//span[@class='mat-mdc-button-touch-target']")
                )
            )
            time.sleep(2)
            username_field.send_keys(username)
            password_field.send_keys(password)
            driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
            actions = ActionChains(driver)
            actions.move_to_element(login_button).click().perform()
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.url_changes(url))
            print("Login successful.")
        except Exception as e:
            print(f"Login failed: {e}")
            with open(os.path.join(ASSETS_DIR, 'login_error_page.html'), 'w') as file:
                file.write(driver.page_source)
            driver.save_screenshot(os.path.join(ASSETS_DIR, 'login_error_screenshot.png'))

    driver.save_screenshot(save_path)
    print(f"Screenshot saved at {save_path}")

def compare_screenshots(image1_path, image2_path, diff_path, comparison_report_path, correct_image_path=None):
    """Compare two screenshots and generate a report with dynamic discrepancies."""
    image1 = Image.open(image1_path).convert("RGB")
    image2 = Image.open(image2_path).convert("RGB")

    # Ensure both images have the same size
    if image1.size != image2.size:
        print("Resizing images to match dimensions...")
        image2 = image2.resize(image1.size)

    image1_array = np.array(image1)
    image2_array = np.array(image2)

    min_dimension = min(image1_array.shape[0], image1_array.shape[1])
    win_size = min(7, min_dimension)

    try:
        # Compute SSIM and differences
        score, diff = ssim(image1_array, image2_array, full=True, multichannel=True, win_size=win_size, channel_axis=-1)
        print(f"SSIM score: {score:.4f}")
        difference_percentage = (1 - score) * 100

        if score >= 0.98:
            print("No significant difference detected.")

            # Handle the case of no significant differences
            if correct_image_path:
                diff_image = Image.open(correct_image_path)  # Use provided "no difference" image
            else:
                # Create a placeholder "No difference" image
                diff_image = Image.new("RGB", image1.size, (255, 255, 255))  # White background
                draw = ImageDraw.Draw(diff_image)
                message = "No difference"
                try:
                    font = ImageFont.load_default()  # Use default font
                except IOError:
                    font = ImageFont.load_default()  # Fallback to default font

                # Add "No difference" text
                bbox = draw.textbbox((0, 0), message, font)
                textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]
                position = ((diff_image.width - textwidth) // 2, (diff_image.height - textheight) // 2)
                draw.text(position, message, font=font, fill="green")

            # Save the "No difference" image
            diff_image.save(diff_path)
            discrepancies = []  # No discrepancies in this case

        else:
            # Generate a difference image
            diff_image = Image.fromarray((diff * 255).astype(np.uint8))
            diff_image.save(diff_path)
            print(f"Difference detected with {difference_percentage:.2f}% difference.")

            # Analyze discrepancies only if differences exist
            discrepancies = analyze_diff(diff, image1_array, image2_array)

    except ValueError as e:
        print(f"SSIM calculation failed: {e}")
        return

    # Ensure discrepancies list includes "No discrepancies found" when empty
    if not discrepancies:
        discrepancies.append({
            "id": 0,
            "description": "No discrepancies found between the images."
        })

    # Generate the HTML report
    generate_html_report(image1_path, image2_path, diff_path, comparison_report_path, difference_percentage, discrepancies)


def analyze_diff(diff, image1_array, image2_array):
    """Analyze the difference image and generate dynamic discrepancies."""
    discrepancies = []

    # Use the normalized difference image to determine discrepancies
    diff_normalized = (diff * 255).astype(np.uint8)

    # Detect discrepancies dynamically
    color_mismatches = np.sum(diff_normalized > 30)  # Lower threshold for significant pixel differences
    if color_mismatches > 0:
        discrepancies.append({
            "id": 1,
            "description": f"Detected {color_mismatches} significant pixel differences in the images."
        })

    shifted_areas = np.sum(diff_normalized > 70)  # Adjusted threshold for shifted layout areas
    if shifted_areas > 0:
        discrepancies.append({
            "id": 2,
            "description": f"Detected {shifted_areas} large layout shifts, possibly indicating UI changes."
        })

    missing_elements = np.sum(diff_normalized > 150)  # Threshold for missing elements or rendering issues
    if missing_elements > 0:
        discrepancies.append({
            "id": 3,
            "description": f"Detected {missing_elements} missing or extra elements in the UI, indicating possible rendering issues."
        })

    return discrepancies

def generate_html_report(image1_path, image2_path, diff_path, report_path, difference_percentage, discrepancies):
    """Generates an improved HTML report for screenshot comparison."""
    
    # Convert images to Base64
    image1_base64 = convert_image_to_base64(image1_path)
    image2_base64 = convert_image_to_base64(image2_path)
    diff_image_base64 = convert_image_to_base64(diff_path)

    discrepancies_rows = ""
    for discrepancy in discrepancies:
        discrepancies_rows += f"""
            <tr>
                <td>{discrepancy['id']}</td>
                <td>{discrepancy['description']}</td>
            </tr>
        """
    
    current_date_time = get_current_date()  # Get current date and time dynamically
    with open(report_path, "w") as report_file:
        report_file.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Clymb Comparison Report</title>
            <link rel="icon" href="https://i0.wp.com/clymbup.io/wp-content/uploads/2023/02/icon.png?fit=32%2C32&amp;ssl=1" sizes="32x32">
            <style>
                 body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f9;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                }}
                header {{
                    background-color: #ffffff;
                    color: black;
                    padding: 20px;
                    text-align: center;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    position: sticky;
                    top: 0;
                    width: 100%;
                    bottom: auto;
                }}
                main {{
                    flex-grow: 1;
                    margin: 20px auto;
                    padding: 20px;
                    background: white;
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                }}
                h1, h2 {{
                    color: #333;
                }}
                .section {{
                    margin-bottom: 30px;
                }}
                .image-comparison {{
                    display: flex;
                    justify-content: space-between;
                }}
                .image-container {{
                    text-align: center;
                    max-width: 48%;
                }}
                #image-container-data{{ 
                    text-align: center;
                    margin: 0 auto;
                    display: block;
                    width: fit-content;
                }}
                img {{
                    max-width: 100%;
                    border-radius: 5px;
                }}
                .progress-bar-container {{
                    margin: 20px 0;
                    width: 100%;
                    background: #e0e0e0;
                    border-radius: 10px;
                    overflow: hidden;
                }}
                .progress-bar {{
                    height: 20px;
                    line-height: 20px;
                    color: white;
                    text-align: center;
                    border-radius: 10px;
                    transition: width 0.5s;
                }}
                .green {{ background: #28a745; }}
                .yellow {{ background: #ffc107; }}
                .orange {{ background: #fd7e14; }}
                .red {{ background: #dc3545; }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                table, th, td {{
                    border: 1px solid #ddd;
                }}
                th, td {{
                    padding: 10px;
                    text-align: left;
                }}
                th {{
                    background-color: #f4f4f9;
                }}
                footer {{
                    text-align: center;
                    color: #777;
                    margin-top: 30px;
                    padding: 10px;
                    background: #f1f1f1;
                }}
                .diff-image {{
                    display: block; 
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <header>
                <h1>Live and Dev Site Comparison Report</h1>
            </header>
            <main>
                <div class="section">
                    <h2>Difference Percentage ({difference_percentage:.2f}%)</h2>
                    <div class="progress-bar-container">
                        <div class="progress-bar {get_color_for_percentage(difference_percentage)}" style="width: {difference_percentage:.2f}%;"></div>
                    </div>
                </div>
                <div class="section">
                    <h2>Images</h2>
                    <div class="section">
                        <div class="image-comparison">
                            <div class="image-container">
                                <h3>Image 1 (Dev Environment)</h3>
                                <img src="data:image/png;base64,{image1_base64}" alt="Dev Screenshot">
                            </div>
                            <div class="image-container">
                                <h3>Image 2 (Live Environment)</h3>
                                <img src="data:image/png;base64,{image2_base64}" alt="Live Screenshot">
                            </div>
                        </div>
                    </div>
                    <div class="section">
                        <h2>Highlighted Differences</h2>
                        <div class="image-container" style="text-align: center;" id="image-container-data">
                            <h3>Difference Image</h3>
                            <div style="width:100%;"><img src="data:image/png;base64,{diff_image_base64}" alt="Difference Image" class="diff-image"></div>
                        </div>
                    </div>
                </div>
                <div class="section">
                    <h2>Discrepancies</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Discrepancy #</th>
                                <th>Description</th>
                            </tr>
                        </thead>
                        <tbody>
                            {discrepancies_rows}
                        </tbody>
                    </table>
                </div>
                <footer>
                    Report generated on {current_date_time}
                </footer>
            </main>
        </body>
        </html>
        """)

def get_color_for_percentage(percentage):
    """Return the color class based on the percentage of differences."""
    if percentage == 0:
        return "green"
    elif 0 < percentage <= 20:
        return "yellow"
    elif 20 < percentage <= 50:
        return "orange"
    else:
        return "red"
    
    
def main():
    with driver() as browser:
        dev_url = "https://clymbadmin.evdpl.com/account/login"
        live_url = "https://clymbup.app#/"

        # Update paths to use assets folder
        dev_screenshot = os.path.join(ASSETS_DIR, "dev_screenshot.png")
        live_screenshot = os.path.join(ASSETS_DIR, "live_screenshot.png")

        diff_image = os.path.join(ASSETS_DIR, "difference.png")
        comparison_report = os.path.join(REPORTS_DIR, "comparison_report.html")

        # Path to "no significant difference" image in assets folder
        correct_image_path = os.path.join(ASSETS_DIR, "no-difference.png")

        # Static username and password
        username = "your_username"  # replace with your actual username
        password = "your_password"  # replace with your actual password

        print("Capturing screenshots for Dev and Live environments...")
        capture_screenshot(dev_url, dev_screenshot, browser, login_required=True, username=username, password=password)
        capture_screenshot(live_url, live_screenshot, browser, login_required=True, username=username, password=password)

        print("Comparing screenshots for Dev and Live environments...")
        compare_screenshots(dev_screenshot, live_screenshot, diff_image, comparison_report, correct_image_path=correct_image_path)

if __name__ == "__main__":
    main()
