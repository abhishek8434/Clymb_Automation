import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from selenium import webdriver
from pages.login import login_to_application
from utils.wall_of_wonder_locators import wall_of_wonder_create, click_on_add_photo, random_photo_select, click_on_wall_to_enter_text, make_post, success_message

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


@given('the student is logged into the application')
def step_impl(context):
    """Step for logging in to the application."""
    
    context.driver = get_driver()  # Use the get_driver function for Chrome WebDriver instance
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
