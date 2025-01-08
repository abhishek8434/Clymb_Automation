from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from dotenv import load_dotenv
import os
import time

def login_to_application(driver):
    """
    Logs into the application using credentials from environment variables.

    Args:
        driver (webdriver): Selenium WebDriver instance.

    Returns:
        None
    """
    # Load environment variables
    load_dotenv()

    # Get login details
    url = os.getenv("BASE_URL")
    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    # Navigate to the URL
    driver.get(url)

    # Step 1: Login
    try:
        email_field = 'email'
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, email_field))
        )
        email_field.send_keys(username)
        
        # Password field xpath fetch and fill password
        password_field= 'password'
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, password_field))
        )  
        password_field.send_keys(password)

        # Submit button xpath fetch and click on button
        login_button = "//button[@type='submit']"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, login_button))
        )
        login_button.click()
        
        compass_dashboard_audio_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[1]/i[2]'
        compass_dashboard_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, compass_dashboard_audio_xpath))
        )

        # Wait for login process to complete
        time.sleep(5)
    except Exception as e:
        print(f"Error during login: {e}")
