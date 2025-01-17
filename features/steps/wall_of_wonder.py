import time
from behave import given, when, then
from pages.login import login_to_application
from utils.wall_of_wonder_locators import wall_of_wonder_create, click_on_add_photo, random_photo_select, click_on_wall_to_enter_text, make_post, success_message
from utils.drivers import setup_driver


@given('the student is logged into the application')
def step_impl(context):
    """Step for logging in to the application."""
    
    context.driver = setup_driver()  # Use the get_driver function for Chrome WebDriver instance
    context.driver.maximize_window()
    login_to_application(context.driver)


@when('the student creates a new wall of wonder')
def step_impl(context):
    """Step for creating a new wall of wonder."""
    wall_of_wonder_create(context.driver)


@when('the student enters text on the wall')
def step_impl(context):
    """Step for submitting the wall."""
    click_on_wall_to_enter_text(context.driver)


@when('the student adds a photo to the wall')
def step_impl(context):
    """Step for clicking to add a photo."""
    click_on_add_photo(context.driver)


@when('the student selects a random photo')
def step_impl(context):
    """Step for selecting a random photo."""
    random_photo_select(context.driver)
    time.sleep(2)


@when('the student makes a post')
def step_impl(context):
    """Step for making a post."""
    make_post(context.driver)


@then('the post should be successfully created')
def step_impl(context):
    """Step to verify the post creation."""
    success_message(context.driver)
    time.sleep(5)
    context.driver.quit()
