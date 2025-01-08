from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from dotenv import load_dotenv
import os
import time
import logging

# Load environment variables
load_dotenv()

def login_to_application(driver):
    """
    Logs into the application using credentials from environment variables.

    Args:
        driver (webdriver): Selenium WebDriver instance.

    Returns:
        None
    """
    # Get login details from environment variables
    url = os.getenv("BASE_URL")
    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    # Ensure the required environment variables are available
    if not url or not username or not password:
        logging.error("Missing environment variables. Please check .env file.")
        raise ValueError("Required environment variables are missing.")

    # Navigate to the URL
    driver.get(url)

    try:
        logging.info(f"Starting login to {url} with username: {username}")

        # Step 1: Enter email
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        )
        email_field.send_keys(username)

        # Step 2: Enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )  
        password_field.send_keys(password)

        # Step 3: Click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        # Step 4: Wait for compass dashboard to load and become clickable
        compass_dashboard_audio_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[1]/i[2]'
        WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, compass_dashboard_audio_xpath))
        )

        # Log successful login
        logging.info(f"Login successful, current URL: {driver.current_url}")

        # Optional: Wait for any additional asynchronous loading or actions after login
        time.sleep(5)

    except Exception as e:
        logging.error(f"Error during login: {e}")
        print(f"Error during login: {e}")
