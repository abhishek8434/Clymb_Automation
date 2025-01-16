import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.forget_password import navigate_to_login_page, click_on_forget_password, enter_details_on_field, click_on_reset_button, verify_message_after_reset



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


@given('Student is on login page')
def step_impl(context):
    
    context.driver = get_driver()
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
