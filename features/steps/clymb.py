from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import logging
from behave import given, when, then
from utils.locators import (
    click_random_emotion, click_random_slider, select_random_mood, compass_dashboard_audio,
    first_next_button, second_next_button, third_next_button, fourth_next_button, fifth_next_button, submit_button,
    ask_for_help
)
from utils.audio import select_audio_emotions, first_audio_homepage
from utils.responsible_decison_making import select_responsible_decision_making
from utils.self_management import handle_self_management
from utils.social_awareness import select_social_awareness_option
from utils.emotions_function import relationship_skills
from utils.aftermood import aftermood
from pages.login import login_to_application
from pages.invalid_login import login_with_invalid_credentials    

logging.basicConfig(level=logging.INFO)


def get_driver():
    """
    Returns a WebDriver instance for Chrome.
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    chrome_options.add_argument('--no-sandbox')  # Disable sandbox for running in Docker
    chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource issues
    chrome_options.add_argument('--remote-debugging-port=9222')  # Fix DevToolsActivePort issue
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--use-gl=swiftshader')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument("--disable-setuid-sandbox")


    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    return driver


@given('the student logs into the application')
def step_login_to_application(context):
    logging.info("Initializing the driver and logging into the application...")
    
    context.driver = get_driver()
    context.driver.maximize_window()
    login_to_application(context.driver)
    time.sleep(5)
    logging.info("Login successful.")


@when('the student interacts with the Compass Dashboard Audio')
def step_compass_dashboard_audio(context):
    compass_dashboard_audio(context.driver)


@when('the student clicks on the audio button')
def step_first_audio_homepage(context):
    first_audio_homepage(context.driver)


@when('the student selects a random emotion')
def step_click_random_emotion(context):
    click_random_emotion(context.driver)


@when('the student interacts with a random slider')
def step_click_random_slider(context):
    click_random_slider(context.driver)


@when('the student clicks the first \'Next\' button')
def step_first_next_button(context):
    first_next_button(context.driver)


@when('the student selects a random mood')
def step_select_random_mood(context):
    select_random_mood(context.driver)


@when('the student selects audio emotions')
def step_select_audio_emotions(context):
    select_audio_emotions(context.driver)


@when('the student clicks the second \'Next\' button')
def step_second_next_button(context):
    second_next_button(context.driver)


@when('the student checks for the \'Ask For Help\' popup')
def step_ask_for_help(context):
    ask_for_help(context.driver)


@when('the student selects responsible decision making')
def step_select_responsible_decision_making(context):
    select_responsible_decision_making(context.driver)


@when('the student clicks the third \'Next\' button')
def step_third_next_button(context):
    third_next_button(context.driver)


@when('the student handles self-management actions')
def step_handle_self_management(context):
    handle_self_management(context.driver)


@when('the student clicks the fourth \'Next\' button')
def step_fourth_next_button(context):
    fourth_next_button(context.driver)


@when('the student selects a social awareness option')
def step_select_social_awareness_option(context):
    select_social_awareness_option(context.driver)


@when('the student clicks the fifth \'Next\' button')
def step_fifth_next_button(context):
    fifth_next_button(context.driver)


@when('the student selects relationship skills options')
def step_relationship_skills(context):
    relationship_skills(context.driver)


@then('the student submits the form')
def step_submit_button(context):
    submit_button(context.driver)


@then('the student interacts with the final modal or resource popup')
def step_aftermood(context):
    aftermood(context.driver)
    time.sleep(2)


def before_all(context):
    """
    Set up context variables or configurations before all tests.
    """
    context.browser = 'chrome'  # Default browser


def after_all(context):
    """
    Tear down the WebDriver instance after all tests are complete.
    """
    if hasattr(context, 'driver'):
        logging.info("Quitting the browser...")
        context.driver.quit()
        
# Negative Flow

@given('Student try to log into the application with invalid credentials')
def step_invalid_login(context):
    
    context.driver = get_driver()
    context.driver.maximize_window()
    login_with_invalid_credentials(context.driver)  # A function where incorrect credentials are used
    time.sleep(5)

@then('Student should see a login failure message on screen')
def step_check_login_failure(context):
    
    # Use the correct XPath expression to find the error message
    error_message_element = context.driver.find_element(By.XPATH, "//div[normalize-space()='Invalid username or password please try again.']")
    # Get the text from the error message element
    error_message = error_message_element.text
    # Assert that the error message is as expected
    assert "Invalid username or password" in error_message
    
    logging.info(error_message)
    context.driver.quit()

