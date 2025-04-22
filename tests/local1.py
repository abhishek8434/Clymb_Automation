import os
import time
import logging
from selenium import webdriver
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SCREENSHOT_DIR = os.path.abspath("screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Device resolutions to test
DEVICE_RESOLUTIONS = {
    "Samsung_S20_Ultra": (412, 915),
    "iPhone_12_Pro": (390, 844),
    # "iPhone_13": (1170, 2532),
    "iPhone_14_Pro_Max": (430, 932),
    # "iPhone_15": (1179, 2556),
    "iPhone_X": (375, 812)
}

def capture_full_page_screenshot(driver, name, max_scroll_height=None):
    """Capture full-page screenshots while hiding the fixed navbar."""
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}_full.png")
    full_width = driver.execute_script("return document.documentElement.scrollWidth")
    viewport_height = driver.execute_script("return window.innerHeight")
    
    # Dynamically detect navbar height
    navbar_height = driver.execute_script("""
        let nav = document.querySelector('.fixed-header, .sticky, .back-to-top');
        return nav ? nav.offsetHeight : 0;
    """)
    
    # Hide navbar before taking screenshots
    driver.execute_script("""
    let elements = document.querySelectorAll('.fixed-header, .sticky, .back-to-top');
    elements.forEach(el => el.style.display = 'none');
    """)
    
    prev_height = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        logging.info(f"Detected Page Height: {new_height}")
        if new_height == prev_height:
            break  
        prev_height = new_height
    
    total_height = new_height if not max_scroll_height else min(new_height, max_scroll_height)
    stitched_image = Image.new('RGB', (full_width, total_height))
    
    scroll_position = 0
    part = 0
    y_offset = 0
    part_paths = []
    
    while scroll_position < total_height:
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(3)  # Ensure elements are fully rendered
        
        part_path = os.path.join(SCREENSHOT_DIR, f"{name}_part{part}.png")
        driver.save_screenshot(part_path)
        part_paths.append(part_path)
        part_img = Image.open(part_path).convert("RGB")
        
        # Crop navbar only after the first screenshot
        if part > 0:
            part_img = part_img.crop((0, navbar_height, full_width, part_img.height))
        
        stitched_image.paste(part_img, (0, y_offset))
        y_offset += part_img.height
        logging.info(f"Scrolled {scroll_position}px ({(scroll_position / total_height) * 100:.2f}%)")
        
        scroll_position = driver.execute_script("return window.scrollY + window.innerHeight")  # Scroll dynamically
        part += 1
        
        if scroll_position >= total_height:
            break  
    
    # Restore navbar visibility
    driver.execute_script("""
    let elements = document.querySelectorAll('.fixed-header, .sticky, .back-to-top');
    elements.forEach(el => el.style.display = '');
    """)
    
    stitched_image.save(screenshot_path)
    logging.info(f"✅ Full-page screenshot saved: {screenshot_path}")
    
    # Delete part images after final image is created
    for part_path in part_paths:
        if os.path.exists(part_path):
            os.remove(part_path)
    
    return screenshot_path


# WebDriver setup
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")

for device, (width, height) in DEVICE_RESOLUTIONS.items():
    logging.info(f"Testing on {device} with resolution {width}x{height}")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(width, height)
    driver.get("https://eatanceapp.com/")  # Replace with your URL
    time.sleep(5)
    capture_full_page_screenshot(driver, f"{device}_screenshot")
    driver.quit()
    logging.info(f"✅ Completed screenshot for {device}\n")
