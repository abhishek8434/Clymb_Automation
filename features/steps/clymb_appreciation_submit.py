import time
from behave import given, when, then
from selenium import webdriver
from pages.login import login_to_application
from pages.invalid_login import login_with_invalid_credentials        
from utils.appreciation import randomly_select_appreciation, submit, appreciation_audio, scrollPage
from utils.audio import second_audio_homepage
from selenium.webdriver.common.by import By
import logging


# Positive Flow

@given('I am logged into the application')
def step_login(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    login_to_application(context.driver)
    time.sleep(5)


@when('I scroll to the end of the page')
def step_scroll_page(context):
    scrollPage(context.driver)


@when('I click on the appreciation audio button')
def step_click_appreciation_audio(context):
    appreciation_audio(context.driver)


@when('I click on the appreciation log audio button')
def step_click_log_audio(context):
    second_audio_homepage(context.driver)


@when('I select an appreciation randomly')
def step_select_appreciation(context):
    randomly_select_appreciation(context.driver)


@then('I submit the appreciation')
def step_submit_appreciation(context):
    submit(context.driver)
    context.driver.quit()


# Negative Flow

@given('I try to log into the application with invalid credentials')
def step_invalid_login(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    login_with_invalid_credentials(context.driver)  # A function where incorrect credentials are used
    time.sleep(5)

@then('I should see a login failure message')
def step_check_login_failure(context):
    
    # Use the correct XPath expression to find the error message
    error_message_element = context.driver.find_element(By.XPATH, "//div[normalize-space()='Invalid username or password please try again.']")
    # Get the text from the error message element
    error_message = error_message_element.text
    # Assert that the error message is as expected
    assert "Invalid username or password" in error_message
    
    logging.info(error_message)
    context.driver.quit()



