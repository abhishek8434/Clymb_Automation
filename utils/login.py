from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        email_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Wait for login process to complete
        time.sleep(5)
    except Exception as e:
        print(f"Error during login: {e}")
