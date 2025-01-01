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
from utils.aftermood import aftermood
from pages.login import login_to_application     
from utils.conditionfornegative import (reload_check_responsible_decision_making, 
                                        reload_check_relationship_skills, reload_check_self_management, 
                                        reload_check_social_awareness, reload_check_self_awareness)
from pages.logout import logout_to_application

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def driver():
    """Initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_workflow(driver):
    """Execute the full workflow in sequence."""

    # Step 1: Login to the application
    login_to_application(driver)
    time.sleep(5)

    # Fetch heading text using the helper functions to check which section is active
    heading_text_self_awareness = reload_check_self_awareness(driver)
    heading_text_responsible_decision_making = reload_check_responsible_decision_making(driver)
    heading_text_self_management = reload_check_self_management(driver)
    heading_text_social_awareness = reload_check_social_awareness(driver)
    heading_text_relationship_skills = reload_check_relationship_skills(driver)

    # Step 2: Compare headings and ensure only the correct one runs
    if heading_text_self_awareness == "Self-Awareness":
        print("Heading is correct for Self-Awareness.")

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

        # Step 9: Check for Ask For Help Popup
        ask_for_help(driver)

        # Step 10: Select Responsible Decision Making
        select_responsible_decision_making(driver)

        # Step 11: Click the Third 'Next' Button
        third_next_button(driver)

        # Step 12: Handle Self-Management Actions
        handle_self_management(driver)

        # Step 13: Click the Fourth 'Next' Button
        fourth_next_button(driver)

        # Step 14: Select Social Awareness Option
        select_social_awareness_option(driver)

        # Step 15: Click the Fifth 'Next' Button
        fifth_next_button(driver)

        # Step 16: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 17: Submit the Form
        submit_button(driver)

        # Step 18: Close the Final Modal or open resource popup
        aftermood(driver)
        time.sleep(2)

    elif heading_text_responsible_decision_making == "Responsible Decision-Making Skill":
        print("Heading is correct for Responsible Decision-Making.")
        
        # Step 10: Select Responsible Decision Making
        select_responsible_decision_making(driver)

        # Step 11: Click the Third 'Next' Button
        third_next_button(driver)

        # Step 12: Log out and log back in to refresh page
        logout_to_application(driver)
        login_to_application(driver)

        # Step 13: Check for the Self-Management Heading after page refresh
        driver.refresh()
        reload_check_self_management(driver)

        # Step 14: Handle Self-Management Actions
        handle_self_management(driver)

        # Step 15: Click the Fourth 'Next' Button
        fourth_next_button(driver)

        # Step 16: Log out and log back in to refresh page
        logout_to_application(driver)
        login_to_application(driver)

        # Step 17: Check for the Social Awareness Heading after page refresh
        driver.refresh()
        reload_check_social_awareness(driver)

        # Step 18: Select Social Awareness Option
        select_social_awareness_option(driver)

        # Step 19: Click the Fifth 'Next' Button
        fifth_next_button(driver)

        # Step 20: Log out and log back in to refresh page
        logout_to_application(driver)
        login_to_application(driver)
        
        # Step 21: Check for the Relationship Skills Heading after page refresh
        driver.refresh()
        reload_check_relationship_skills(driver)

        # Step 22: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 23: Submit the Form
        submit_button(driver)

        # Step 24: Close the Final Modal or open resource popup
        aftermood(driver)
        time.sleep(2)

    elif heading_text_self_management == "Self-Management":
        print("Heading is correct for Self-Management.")

        # Step 12: Handle Self-Management Actions
        handle_self_management(driver)

        # Step 13: Click the Fourth 'Next' Button
        fourth_next_button(driver)

        # Step 14: Select Social Awareness Option
        select_social_awareness_option(driver)

        # Step 15: Click the Fifth 'Next' Button
        fifth_next_button(driver)

        # Step 16: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 17: Submit the Form
        submit_button(driver)

        # Step 18: Close the Final Modal or open resource popup
        aftermood(driver)
        time.sleep(2)

    elif heading_text_social_awareness == "Social Awareness":
        print("Heading is correct for Social Awareness.")

        # Step 14: Select Social Awareness Option
        select_social_awareness_option(driver)

        # Step 15: Click the Fifth 'Next' Button
        fifth_next_button(driver)

        # Step 16: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 17: Submit the Form
        submit_button(driver)

        # Step 18: Close the Final Modal or open resource popup
        aftermood(driver)
        time.sleep(2)

    elif heading_text_relationship_skills == "Relationship Skills":
        print("Heading is correct for Relationship Skills.")

        # Step 16: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 17: Submit the Form
        submit_button(driver)

        # Step 18: Close the Final Modal or open resource popup
        aftermood(driver)
        time.sleep(2)
    else:
        print("No heading matched the expected values.")
