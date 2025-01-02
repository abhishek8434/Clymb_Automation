import pytest
import time
from selenium import webdriver
from pages.login import login_to_application    
from utils.wall_of_wonder_locators import wall_of_wonder_create, click_on_add_photo, random_photo_select, click_on_submit_wall, make_post



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
    
    
    wall_of_wonder_create(driver)
    
    click_on_submit_wall(driver)
    
    click_on_add_photo(driver)
    
    random_photo_select(driver)    
    time.sleep(2)
    
    make_post(driver)
    
    time.sleep(5)