import os
import time
import numpy as np
import logging
from selenium import webdriver
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SCREENSHOT_DIR = os.path.abspath("screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def capture_full_page_screenshot(driver, name, max_scroll_height=None):
    """Capture full-page screenshots while hiding the fixed navbar."""
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}_full.png")
    full_width = driver.execute_script("return document.documentElement.scrollWidth")
    viewport_height = driver.execute_script("return window.innerHeight")

    # Manually set navbar height if needed
    navbar_height = 80  

    # Hide navbar before taking screenshots
    driver.execute_script("""
    let elements = document.querySelectorAll('.fixed-header, .sticky, .back-to-top');
    elements.forEach(el => el.style.display = 'none');
    """)

    # Determine total scrollable height
    prev_height = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        logging.info(f"Detected Page Height: {new_height}")
        if new_height == prev_height:
            break  
        prev_height = new_height

    total_height = new_height
    if max_scroll_height:
        total_height = min(total_height, max_scroll_height)

    # Start capturing sections
    stitched_image = Image.new('RGB', (full_width, total_height))
    
    scroll_position = 0
    part = 0
    y_offset = 0
    
    while scroll_position < total_height:
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(2)  # Allow content to load

        # Capture and store the screenshot
        part_path = os.path.join(SCREENSHOT_DIR, f"{name}_part{part}.png")
        driver.save_screenshot(part_path)
        part_img = Image.open(part_path).convert("RGB")

        # Resize width for consistency
        part_img = part_img.resize((full_width, part_img.height), Image.Resampling.LANCZOS)

        # Crop the navbar from all images except the first one
        if part > 0:
            part_img = part_img.crop((0, navbar_height, full_width, part_img.height))

        # Paste each captured section correctly
        stitched_image.paste(part_img, (0, y_offset))
        y_offset += part_img.height

         # Log scroll progress
        percentage_scrolled = (scroll_position / total_height) * 100
        logging.info(f"Scrolled {scroll_position}px ({percentage_scrolled:.2f}%)")


        # Update scroll position properly
        scroll_position += part_img.height
        part += 1
        
        if scroll_position >= total_height:
            break  

    # Restore navbar after screenshots
    driver.execute_script("""
    let elements = document.querySelectorAll('.fixed-header, .sticky, .back-to-top');
    elements.forEach(el => el.style.display = '');
    """)

    stitched_image.save(screenshot_path)
    logging.info(f"✅ Full-page screenshot saved: {screenshot_path}")
    return screenshot_path


# WebDriver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://eatanceapp.com/")  # Replace with your URL
time.sleep(5)

# Set max_scroll_height to limit scrolling, or None for full-page scrolling
capture_full_page_screenshot(driver, "final_screenshot", max_scroll_height=6648)

driver.quit()
