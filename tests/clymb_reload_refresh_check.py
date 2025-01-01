import pytest
import time
from selenium import webdriver
from utils.locators import click_random_emotion, click_random_slider, select_random_mood, compass_dashboard_audio
from utils.locators import first_next_button, second_next_button, third_next_button, fourth_next_button, fifth_next_button, submit_button
from utils.locators import ask_for_help
from utils.audio import select_audio_emotions
from utils.responsible_decison_making import select_responsible_decision_making
from utils.self_management import handle_self_management
from utils.social_awareness import select_social_awareness_option
from utils.emotions_function import relationship_skills
from utils.self_management import handle_self_management
from utils.aftermood import aftermood
from pages.login import login_to_application     
from utils.conditionfornegative import (reload_check_responsible_decision_making, reload_check_relationship_skills, 
                                        reload_check_self_management, reload_check_social_awareness)
from pages.logout import logout_to_application


@pytest.fixture(scope="module")
def driver():
    """Initialize and quit the WebDriver."""
    # Initialize Chrome WebDriver and maximize the window for the session
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_workflow(driver):
    """Execute the full workflow in sequence."""

    # Step 1: Login to the application
    login_to_application(driver)
    time.sleep(5)  # Allowing time for the application to load

    # Step 2: Interact with Compass Dashboard Audio
    compass_dashboard_audio(driver)

    # Step 3: Select a Random Emotion
    click_random_emotion(driver)

    # Step 4: Interact with a Random Slider
    click_random_slider(driver)

    # Step 5: Click the First 'Next' Button
    first_next_button(driver)

    # Step 6: Select a Random Mood
    select_random_mood(driver)

    # Step 7: Select Audio Emotions
    select_audio_emotions(driver)

    # Step 8: Click the Second 'Next' Button
    second_next_button(driver)

    # Step 9: Check for "Ask for Help" Popup
    ask_for_help(driver)

    # Step 10: Refresh the page and check for the "Responsible Decision Making" section
    driver.refresh()
    reload_check_responsible_decision_making(driver)

    # Step 11: Logout and Login Again to simulate session refresh
    logout_to_application(driver)
    login_to_application(driver)
    driver.refresh()  # Refreshing the page after re-login
    reload_check_responsible_decision_making(driver)

    # Step 12: Select Responsible Decision Making
    select_responsible_decision_making(driver)

    # Step 13: Click the Third 'Next' Button
    third_next_button(driver)

    # Step 14: Logout and login to refresh session for Self-Management
    logout_to_application(driver)
    login_to_application(driver)
    driver.refresh()  # Refreshing the page after re-login
    reload_check_self_management(driver)

    # Step 15: Handle Self-Management Actions
    handle_self_management(driver)

    # Step 16: Click the Fourth 'Next' Button
    fourth_next_button(driver)

    # Step 17: Logout and login to refresh session for Social Awareness
    logout_to_application(driver)
    login_to_application(driver)
    driver.refresh()  # Refreshing the page after re-login
    reload_check_social_awareness(driver)

    # Step 18: Select Social Awareness Option
    select_social_awareness_option(driver)

    # Step 19: Click the Fifth 'Next' Button
    fifth_next_button(driver)

    # Step 20: Logout and login to refresh session for Relationship Skills
    logout_to_application(driver)
    login_to_application(driver)
    driver.refresh()  # Refreshing the page after re-login
    reload_check_relationship_skills(driver)

    # Step 21: Select Relationship Skills Options
    relationship_skills(driver)

    # Step 22: Submit the Form
    submit_button(driver)

    # Step 23: Close the Final Modal or open resource popup
    aftermood(driver)
    time.sleep(2)  # Allowing time for the final modal to close


if __name__ == "__main__":
    from selenium import webdriver
