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
from utils.condition_for_negative_flow import (reload_check_responsible_decision_making, 
                                        reload_check_relationship_skills, reload_check_self_management, 
                                        reload_check_social_awareness, reload_check_self_awareness)
from pages.logout import logout_to_application
from utils.audio import first_audio_homepage

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
        
        #Step 3 : Click on Audio Button 
        first_audio_homepage(driver)

        # Step 4: Select a Random Emotion
        click_random_emotion(driver)

        # Step 5: Interact with a Random Slider
        click_random_slider(driver)

        # Step 6: Click the First 'Next' Button
        first_next_button(driver)

        # Step 7: Select a Random Mood
        select_random_mood(driver)

        # Step 8: Select Audio Emotions
        select_audio_emotions(driver)

        # Step 9: Click the Second 'Next' Button
        second_next_button(driver)

        # Step 10: Check for Ask For Help Popup
        ask_for_help(driver)

        # Step 11: Select Responsible Decision Making
        select_responsible_decision_making(driver)

        # Step 12: Click the Third 'Next' Button
        third_next_button(driver)

        # Step 13: Handle Self-Management Actions
        handle_self_management(driver)

        # Step 14: Click the Fourth 'Next' Button
        fourth_next_button(driver)

        # Step 15: Select Social Awareness Option
        select_social_awareness_option(driver)

        # Step 16: Click the Fifth 'Next' Button
        fifth_next_button(driver)

        # Step 17: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 18: Submit the Form
        submit_button(driver)

        # Step 19: Close the Final Modal or open resource popup
        aftermood(driver)
        
        time.sleep(2)
        ask_for_help(driver)

    elif heading_text_responsible_decision_making == "Responsible Decision-Making Skill":
        print("Heading is correct for Responsible Decision-Making.")
        
        # Step 11: Select Responsible Decision Making
        select_responsible_decision_making(driver)

        # Step 12: Click the Third 'Next' Button
        third_next_button(driver)

        # Step 13: Handle Self-Management Actions
        handle_self_management(driver)

        # Step 14: Click the Fourth 'Next' Button
        fourth_next_button(driver)

        # Step 15: Select Social Awareness Option
        select_social_awareness_option(driver)

        # Step 16: Click the Fifth 'Next' Button
        fifth_next_button(driver)

        # Step 17: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 18: Submit the Form
        submit_button(driver)

        # Step 19: Close the Final Modal or open resource popup
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
        
        ask_for_help(driver)

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
        
        ask_for_help(driver)

    elif heading_text_relationship_skills == "Relationship Skills":
        print("Heading is correct for Relationship Skills.")

        # Step 16: Select Relationship Skills Options
        relationship_skills(driver)

        # Step 17: Submit the Form
        submit_button(driver)

        # Step 18: Close the Final Modal or open resource popup
        aftermood(driver)
        time.sleep(2)
        
        ask_for_help(driver)
    else:
        print("No heading matched the expected values.")
