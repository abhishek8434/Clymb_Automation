from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from dotenv import load_dotenv
import os
import time
import logging
from pages.logout import logout_to_application


def login_to_application_loop(driver):
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
    url = os.getenv("LIVE_URL")
 
    
    # Define login credentials from environment variables
    login_details = [
        {"username": os.getenv("LIVE_EMAIL"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL1"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL2"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL3"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL4"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL5"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL6"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL7"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("LIVE_EMAIL8"), "password": os.getenv("PASSWORD")},

    ]
        
    for credentials in login_details:
        # Navigate to the URL
        driver.get(url)

        try:
            # Step 1: Enter email
            email_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'email'))
            )
            email_field.send_keys(credentials["username"])
            # Step 2: Enter password
            password_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'password'))
            )  
            password_field.send_keys(credentials["password"])

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
            
            logout_to_application(driver)

        except Exception as e:
            logging.error(f"Error during login: {e}")
            print(f"Error during login: {e}")