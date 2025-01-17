import time
from behave import given, when, then
from pages.login import login_to_application
from utils.sel_checkpoint import select_sel, first_question, next_button, submit_button, verify_message_after_submit, extract_question_count
import logging
from utils.drivers import setup_driver

@given('Student is on login page to fill SEL form')
def step_impl(context):
    context.driver = setup_driver()
    context.driver.maximize_window()
    login_to_application(context.driver)
    time.sleep(5)


@when('Student clicks on SEL Checkpoint button')
def step_impl(context):
    select_sel(context.driver)


@when('Student completes all questions and navigates through them')
def step_impl(context):
    # Extract the dynamic question count
    total_questions = extract_question_count(context.driver)
    logging.info(f"Extracted question count is: '{total_questions}'")
    if total_questions == 0:
        raise Exception("Unable to determine the total number of questions.")
    
    # Loop through the dynamic number of questions
    for question_number in range(1, total_questions + 1):
        first_question(context.driver)  # Select a random option for the current question
        if question_number < total_questions:
            next_button(context.driver)  # Click next for all but the last question
        time.sleep(1)

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
