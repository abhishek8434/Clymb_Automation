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
    url = os.getenv("ADMIN_URL")
    admin_email = os.getenv("ADMIN_EMAIL")
    admin_password = os.getenv("ADMIN_PASSWORD")

    # Navigate to the URL
    driver.get(url)

   
    try:
        # Email field xpath fetch and will fill email 
        admin_email_xpath = '//*[@id="mat-input-0"]'
        admin_email_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, admin_email_xpath))
        )
        admin_email_element.send_keys(admin_email)
        
        # Password field xpath fetch and fill password
        admin_password_xpath= '//*[@id="mat-input-1"]'
        admin_password_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, admin_password_xpath))
        )  
        admin_password_element.send_keys(admin_password)

        # Submit button xpath fetch and click on button
        admin_submit_button_xpath= '/html/body/fuse-root/div/main/app-auth-layout/app-login/section/div/div[2]/div/form/button/span[2]'
        admin_submit_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, admin_submit_button_xpath))
        )
        admin_submit_button_element.click()
           
    except Exception as e:
        print(f"Error during login: {e}")
