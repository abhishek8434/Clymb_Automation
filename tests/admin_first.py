import pytest
import time
from selenium import webdriver
from pages.admin_login import login_to_application        



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