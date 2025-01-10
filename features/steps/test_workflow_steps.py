import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from pages.login import login_to_application
from pages.admin_login import login_to_application_admin
from utils.locators import ask_for_help_1
from utils.verify_ask_for_help_locator import verify_names, verify_name_admin_notification
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_driver():
    """
    Initializes and returns a Chrome WebDriver instance with predefined options.
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode for CI/CD environments
    chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    chrome_options.add_argument('--no-sandbox')  # Disable sandbox for Docker environments
    chrome_options.add_argument('--disable-dev-shm-usage')  # Handle limited resource issues
    chrome_options.add_argument('--remote-debugging-port=9222')  # Debugging support
    chrome_options.add_argument('--mute-audio')  # Mute audio for automated testing
    chrome_options.add_argument('--use-gl=swiftshader')  # Use SwiftShader for rendering
    chrome_options.add_argument('--disable-software-rasterizer')  # Disable software rasterization

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver


@given('I log in to the main application')
def step_impl_main_app_login(context):
    """Log in to the main application in the first tab."""
    context.driver = get_driver()  # Use the get_driver function for Chrome WebDriver instance
    context.driver.maximize_window()
    login_to_application(context.driver)  # Executes all actions for login on the first tab
    WebDriverWait(context.driver, 10).until(EC.url_changes)  # Wait for URL change after login
    logger.info("Main application login completed.")


@given('I log in to the admin application')
def step_impl_admin_app_login(context):
    """Log in to the admin application in the second tab."""
    # Open a new tab using JavaScript
    context.driver.execute_script("window.open('');")
    
    # Get all window handles and print them for debugging
    windows = context.driver.window_handles
    print(f"Windows before switch: {windows}")
    
    # Check if the new tab has opened
    if len(windows) > 1:
        context.driver.switch_to.window(windows[1])  # Switch to the new tab
    else:
        raise Exception("Admin application tab did not open")
    
    # Wait for the admin login page to load by checking for an element that is present in the admin tab
    # You can replace 'admin_login_element' with a locator specific to the admin page
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "admin_login_element"))  # Replace with a valid locator
    )
    
    login_to_application_admin(context.driver)  # Executes all actions for admin login on the second tab
    
    # Wait for the URL to change (indicating successful login)
    WebDriverWait(context.driver, 10).until(EC.url_changes)
    
    logger.info("Admin application login completed.")


@when('I switch back to the main application')
def step_impl_switch_back_to_main_app(context):
    """Switch back to the main application tab."""
    tabs = context.driver.window_handles
    context.driver.switch_to.window(tabs[0])
    logger.info("Switched back to the main application tab.")


@when('I click "Ask For Help"')
def step_impl_click_ask_for_help(context):
    """Click the 'Ask For Help' link and perform related actions."""
    ask_for_help_xpath = "//a[normalize-space()='Ask For Help']"
    ask_for_help_selected = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ask_for_help_xpath))
    )
    ask_for_help_selected.click()
    ask_for_help_1(context.driver)  # Perform the "Ask For Help" actions
    logger.info("Completed actions in the main application.")


@then('I should be able to extract the name from the main application')
def step_impl_extract_name(context):
    """Extract the name from the main application."""
    extracted_name = verify_names(context.driver)
    context.extracted_name = extracted_name  # Save the extracted name for later verification
    logger.info(f"Extracted name: {extracted_name}")


@when('I switch to the admin application')
def step_impl_switch_to_admin_app(context):
    """Switch to the admin application tab."""
    tabs = context.driver.window_handles
    context.driver.switch_to.window(tabs[1])
    logger.info("Switched to the admin application tab.")


@then('I should verify the extracted name in the admin application')
def step_impl_verify_name_in_admin(context):
    """Verify the extracted name in the admin application."""
    verify_name_admin_notification(context.driver, context.extracted_name)
    logger.info("Name verification completed in the admin tab.")
