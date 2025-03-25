import os
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.logout import logout_to_application

# Load environment variables from .env file
load_dotenv()

# Define login credentials from environment variables
login_details = [
    {"username": os.getenv("LIVE_EMAIL"), "password": os.getenv("PASSWORD")},
    {"username": os.getenv("LIVE_EMAIL1"), "password": os.getenv("PASSWORD1")},
    {"username": os.getenv("LIVE_EMAIL2"), "password": os.getenv("PASSWORD2")},
    {"username": os.getenv("LIVE_EMAIL3"), "password": os.getenv("PASSWORD3")},
    {"username": os.getenv("LIVE_EMAIL4"), "password": os.getenv("PASSWORD4")},
    {"username": os.getenv("LIVE_EMAIL5"), "password": os.getenv("PASSWORD5")},
    {"username": os.getenv("LIVE_EMAIL6"), "password": os.getenv("PASSWORD6")},
    {"username": os.getenv("LIVE_EMAIL7"), "password": os.getenv("PASSWORD7")},
    {"username": os.getenv("LIVE_EMAIL8"), "password": os.getenv("PASSWORD8")},
]
login_url = os.getenv("LIVE_URL")

MAX_RETRIES = 3  # Max number of retries for each login attempt
RETRY_DELAY = 2  # Delay between retries (in seconds)

# Function to log in a user with retry logic
def login_user(credentials):
    driver = webdriver.Chrome() # Ensure chromedriver is installed and accessible
    driver.maximize_window()
    driver.get(login_url)

    # Retry logic for transient errors
    for attempt in range(MAX_RETRIES):
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

            print(f"Login successful for {credentials['username']}")
            time.sleep(2)  # Wait for a moment to ensure login completes
            return True  # If successful, return True

        except Exception as e:
            print(f"Error logging in for {credentials['username']} (Attempt {attempt+1}/{MAX_RETRIES}): {e}")
            time.sleep(RETRY_DELAY)  # Retry after a brief delay

        # Ensure the driver is always closed after each attempt
        finally:
            driver.quit()
            
    # If all retries fail
    print(f"Failed to login for {credentials['username']} after {MAX_RETRIES} attempts.")
    return False

    

# Test for the login functionality with parallel execution
def test_login_users():
    with ThreadPoolExecutor(max_workers=len(login_details)) as executor:
        results = list(executor.map(lambda creds: login_user(creds), login_details))

    failed_logins = [creds['username'] for creds, result in zip(login_details, results) if not result]
    assert not failed_logins, f"Login failed for the following users: {', '.join(failed_logins)}"

# Simple sample test to ensure pytest is working
def test_sample():
    assert True