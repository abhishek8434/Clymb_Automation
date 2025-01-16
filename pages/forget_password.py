from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from dotenv import load_dotenv
import os
import time
import logging

def navigate_to_login_page(driver):
    # Load environment variables from .env file
    load_dotenv()

    # Get login details from environment variables
    url = os.getenv("BASE_URL")
   
    # Navigate to the URL
    driver.get(url)
    # Log successful login
    logging.info(f"User is on login page")

def click_on_forget_password(driver):
    
    forget_passord_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Forgot Your Password ?']"))
    )
    forget_passord_link.click() 
    logging.info(f"User clicked on forget password link ")
    time.sleep(2)
    logging.info(f"User clicked on forget password link and current URL: {driver.current_url}")

def enter_details_on_field(driver):
    username = os.getenv("EMAIL")
    
    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'email'))
    )  
    email_field.send_keys(username)
    
    time.sleep(1)
    
def click_on_reset_button(driver):
    
    reset_password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reset Password']"))
    )
    reset_password_button.click() 
    
def verify_message_after_reset(driver):
   
    time.sleep(2)
    success_message_xpath = "//div[@class='text-success']"
    
    success_message_fetch = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, success_message_xpath))
    )
    
    # Get the text of the success message
    success_message_text = success_message_fetch.text
    
    # Expected success message value
    success_message_value = "A password reset link has been sent to your email."
    
    # Compare the text and print the result
    if success_message_text == success_message_value:
        logging.info("A password reset link has been sent to your email.")
    else:
        logging.info(f"Extracted message: '{success_message_text}'")