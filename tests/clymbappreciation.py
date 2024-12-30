import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
        
from utils.appreciation import randomly_select_appreciation, submit, appreciation_audio, scrollPage

# Load environment variables
load_dotenv()

# Get login details
url = os.getenv("BASE_URL")
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


@pytest.fixture(scope="module")
def driver():
    """Initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_workflow(driver):
    """Execute the full workflow in sequence."""
    driver.get(url)
    time.sleep(2)

    # Step 1: Login
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    email_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)

    #Step 2: Scroll Page to end of page
    scrollPage(driver)
 
    #Step 3: Click on audio button
    appreciation_audio(driver)

    #Step 4: Select Appreciation randomly
    randomly_select_appreciation(driver)

    #Step 5: Click on Done button
    submit(driver)




    