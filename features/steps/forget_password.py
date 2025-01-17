import time
from behave import given, when, then
from pages.forget_password import navigate_to_login_page, click_on_forget_password, enter_details_on_field, click_on_reset_button, verify_message_after_reset
from utils.drivers import setup_driver

@given('Student is on login page')
def step_impl(context):
    
    context.driver = setup_driver()
    context.driver.maximize_window()
    navigate_to_login_page(context.driver)
    time.sleep(5)

@when('Student click on forget password link')
def step_impl(context):
    click_on_forget_password(context.driver)

@when('Student enter email on the field')
def step_impl(context):
    enter_details_on_field(context.driver)

@when('Student click on reset password button')
def step_impl(context):
    click_on_reset_button(context.driver)

@then('Student should see the success message for reset password')
def step_impl(context):
    verify_message_after_reset(context.driver)

# Quit the context.driver after tests
def after_all(context):
    context.driver.quit()
