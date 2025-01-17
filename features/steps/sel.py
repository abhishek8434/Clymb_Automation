import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import login_to_application
from utils.sel_checkpoint import select_sel, first_question, next_button, submit_button, verify_message_after_submit
import logging


def get_driver():
    """ Initializes and returns a Chrome WebDriver instance with predefined options. """
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode for CI/CD environments
    chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    chrome_options.add_argument('--no-sandbox')  # Disable sandbox for Docker environments
    chrome_options.add_argument('--disable-dev-shm-usage')  # Handle limited resource issues
    chrome_options.add_argument('--remote-debugging-port=9222')  # Debugging support
    chrome_options.add_argument('--mute-audio')  # Mute audio for automated testing
    chrome_options.add_argument('--use-gl=swiftshader')  # Use SwiftShader for rendering
    chrome_options.add_argument('--disable-software-rasterizer')  # Disable software rasterization
    chrome_options.add_argument("--disable-setuid-sandbox")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver


@given('Student is on login page to fill SEL form')
def step_impl(context):
    context.driver = get_driver()
    context.driver.maximize_window()
    login_to_application(context.driver)
    time.sleep(5)


@when('Student clicks on SEL Checkpoint button')
def step_impl(context):
    select_sel(context.driver)


@when('Student completes all questions and navigates through them')
def step_impl(context):
    # Loop through the 12 questions
     for question_number in range(1, 13):
        first_question(context.driver)  # Select a random option for the current question
        if question_number < 12:
            next_button(context.driver)  # Click next for questions 1-11iver)  # Click next for questions 1-11    
        time.sleep(1)  # Optional: Adjust delay if needed for UI transitions
        

@then('Student successfully submits the SEL form')
def step_impl(context):
    submit_button(context.driver)

@then('Will verify Success Message')
def step_impl(context):
    verify_message_after_submit(context.driver)
    logging.info("Verified messgae ")
    time.sleep(5) 

def after_all(context):
    """Clean up after all tests."""
    context.driver.quit()
