import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login import login_to_application        
from utils.locators import ask_for_help

@pytest.fixture(scope="module")
def driver():
    """Initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
    
def test_workflow(driver):
    """Execute the full workflow in sequence."""
   
    # Step 1: Login
    login_to_application(driver)
    time.sleep(5)
    
    ask_for_help_xpath = "//a[normalize-space()='Ask For Help']"
    ask_for_help_selected = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ask_for_help_xpath))
        )
    ask_for_help_checked = ask_for_help_selected.click()
    
    ask_for_help(driver)
    
    time.sleep(5)