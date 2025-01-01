import pytest
import time
from selenium import webdriver
from pages.login import login_to_application        
from utils.appreciation import randomly_select_appreciation, submit, appreciation_audio, scrollPage
from utils.audio import second_audio_homepage


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

    #Step 2: Scroll Page to end of page
    scrollPage(driver)
 
    #Step 3: Click on audio button
    appreciation_audio(driver)

    #Step 4 : Click on Appreciation Log Audio Button 
    second_audio_homepage(driver)
        
    #Step 5: Select Appreciation randomly
    randomly_select_appreciation(driver)

    #Step 6: Click on Done button
    submit(driver)




    