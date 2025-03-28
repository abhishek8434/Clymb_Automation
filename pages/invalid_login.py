from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from dotenv import load_dotenv
import os
import time
import logging

def login_with_invalid_credentials(driver):
    """
    Logs into the application using credentials from environment variables.

    Args:
        driver (webdriver): Selenium WebDriver instance.

    Returns:
        None
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get login details from environment variables
    url = os.getenv("BASE_URL")
    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    # Navigate to the URL
    driver.get(url)

    try:
        # Step 1: Enter email
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        )
        email_field.send_keys("incorrect_email")

        
        
        # Step 2: Enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'password'))
        )  
        password_field.send_keys("incorrect_password")

        # Step 3: Click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        # Optional: Wait for any additional asynchronous loading or actions after login
        time.sleep(5)

    except Exception as e:
        logging.error(f"Error during login: {e}")
        print(f"Error during login: {e}")
