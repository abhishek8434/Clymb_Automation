import time
from behave import given, when, then
from pages.login import login_to_application
from utils.appreciation import randomly_select_appreciation, submit, appreciation_audio, scrollPage, your_journey, check_appreciation_log
from utils.condition_for_negative_flow import reload_check_self_awareness
from utils.audio import second_audio_homepage
from utils.drivers import setup_driver

@given('I am logged into the student application')
def step_impl(context):
    
    context.driver = setup_driver()
    context.driver.maximize_window()
    login_to_application(context.driver)
    time.sleep(5)

@when('I scroll the page to the end')
def step_impl(context):
    scrollPage(context.driver)

@when('I select an appreciation audio')
def step_impl(context):
    appreciation_audio(context.driver)
    second_audio_homepage(context.driver)

@when('I submit the appreciation log')
def step_impl(context):
    # Store selected appreciation in context
    selected_appreciation, test_appreciation = randomly_select_appreciation(context.driver)
    context.test_appreciation = test_appreciation  # Store in context
    submit(context.driver)

@when('I navigate to my journey tab')
def step_impl(context):
    your_journey(context.driver)
    time.sleep(2)

@when('I check the self-awareness heading')
def step_impl(context):
    # Capture the heading text and store it in context
    heading_text_self_awareness = reload_check_self_awareness(context.driver)
    context.heading_text_self_awareness = heading_text_self_awareness
    print(f"Heading text: {heading_text_self_awareness}")  # Optional debug log

@then('I should see the appreciation log in my journey')
def step_impl(context):
    # Ensure heading is captured in context
    if hasattr(context, 'heading_text_self_awareness') and context.heading_text_self_awareness == "Self-Awareness":
        check_appreciation_log(context.driver, context.test_appreciation)
    else:
        print("Please complete the form you are in the middle of, so you can't select Appreciation Station")

# Quit the context.driver after tests
def after_all(context):
    context.driver.quit()
