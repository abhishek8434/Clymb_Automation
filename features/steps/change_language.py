import time
from behave import given, when, then
from pages.login import login_to_application
from utils.locators import change_language    
from utils.appreciation import randomly_select_appreciation, submit, appreciation_audio, scrollPage
from utils.audio import second_audio_homepage
import logging
from utils.drivers import setup_driver

logging.basicConfig(level=logging.INFO)


# Positive Flow

@given('I am logged into the application1')
def step_login(context):
   
    context.driver = setup_driver()
    context.driver.maximize_window()
    login_to_application(context.driver)
    time.sleep(5)
    change_language(context.driver)

@when('I scroll to the end of the page1')
def step_scroll_page(context):
    scrollPage(context.driver)


@when('I click on the appreciation audio button1')
def step_click_appreciation_audio(context):
    appreciation_audio(context.driver)


@when('I click on the appreciation log audio button1')
def step_click_log_audio(context):
    second_audio_homepage(context.driver)


@when('I select an appreciation randomly1')
def step_select_appreciation(context):
    randomly_select_appreciation(context.driver)


@then('I submit the appreciation1')
def step_submit_appreciation(context):
    submit(context.driver)
    context.driver.quit()




