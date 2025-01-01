import pytest
from dotenv import load_dotenv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Load environment variables
load_dotenv()


# Get login details from the .env file
URL = os.getenv("URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def test_logindetails(driver):
    """Perform login and validate success."""
    # Locate elements and perform login
    time.sleep(2)
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Use credentials from environment variables
    email_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)
    login_button.click()

    # Wait for login to complete
    time.sleep(5)

    # Assert that login was successful
    assert "dashboard" in driver.current_url or driver.title != "Login", "Login failed"