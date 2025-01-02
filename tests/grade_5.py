import pytest
import time
from selenium import webdriver

from pages.login import login_to_application   
from utils.locators import click_random_emotion, click_random_slider, compass_dashboard_audio
from pages.login import login_to_application   
from utils.audio import first_audio_homepage   
from utils.locators_for_grade_5 import select_audio_emotions, select_random_mood, grade_5_submit, sub_mood_submit , execute_random_action



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
    
    # Step 2: Interact with Compass Dashboard Audio
    compass_dashboard_audio(driver)
    
    #Step 3 : Click on Audio Button 
    first_audio_homepage(driver)

    # Step 4: Select a Random Emotion
    click_random_emotion(driver)

    # Step 5: Interact with a Random Slider
    click_random_slider(driver)
    
    # Step 6: Click on Submit Button
    grade_5_submit(driver)
    
    # Step 7: Select Sub mood
    select_random_mood(driver)
    
    # Step 8: Click on submood audio 
    select_audio_emotions(driver)
    
    # Step 9: Click on submood submit button
    sub_mood_submit(driver)
    
    # Step 10: Aftermood and resources
    execute_random_action(driver)
    
    time.sleep(4)
    
    