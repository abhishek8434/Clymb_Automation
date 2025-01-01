import pytest
import time
from selenium import webdriver
from pages.login import login_to_application        
from utils.appreciation import randomly_select_appreciation, submit, appreciation_audio, scrollPage, your_journey, check_appreciation_log
from utils.condition_for_negative_flow import  reload_check_self_awareness


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

    heading_text_self_awareness = reload_check_self_awareness(driver)
    
    # Step 2: Compare headings and ensure only the correct one runs
    if heading_text_self_awareness == "Self-Awareness":
        print("Heading is correct for Self-Awareness.")
    
        #Step 2: Scroll Page to end of page
        scrollPage(driver)
    
        #Step 3: Click on audio button
        appreciation_audio(driver)

        selected_appreciation, test_appreciation = randomly_select_appreciation(driver)

        #Step 5: Click on Done button
        submit(driver)
        
        your_journey(driver)
        
        # Step 6: Check appreciation log
        # Call the check_appreciation_log function
        check_appreciation_log(driver, test_appreciation)
    else:
        print("Please complete the form you are in middle of form so you can't select Appreciation Station")
        
    
    
    




    