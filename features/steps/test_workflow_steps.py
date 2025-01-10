import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login import login_to_application
from pages.admin_login import login_to_application_admin
from utils.locators import ask_for_help
from utils.verify_ask_for_help_locator import verify_names, verify_name_admin_notification
from behave import given, when, then
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging


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


@given("the user logs into the student application")
def step_login_main_application(context):
    """
    Log into the main application using the provided WebDriver context.
    """
    context.driver = get_driver()
    context.driver.maximize_window()
    login_to_application(context.driver)
    logging.info("Main application login completed.")
    WebDriverWait(context.driver, 10).until(EC.url_changes, "Login did not result in URL change.")


@given("the user opens a new tab for admin login")
def step_open_admin_tab(context):
    """
    Open a new browser tab for admin login and switch to it.
    """
    time.sleep(2)
    logging.info("Opened")
    context.driver.execute_script("window.open('');")
    time.sleep(2)
    logging.info("switched to tab.")
    # Ensure the window handles list has more than 1 item before switching
    WebDriverWait(context.driver, 30).until(
        lambda driver: len(driver.window_handles) > 1, "New tab did not open in time."
    )
    context.tabs = context.driver.window_handles
    logging.info("Tabs available:", context.tabs)
    context.driver.switch_to.window(context.tabs[1])
    logging.info("Opened and switched to admin login tab.")
    


@when("the user logs into the admin application")
def step_login_admin_application(context):
    """
    Log into the admin application in the new tab.
    """
    login_to_application_admin(context.driver)
    logging.info("Admin application login completed.")
    WebDriverWait(context.driver, 10).until(EC.url_changes, "Admin login did not result in URL change.")


@when("the user switches back to the main application")
def step_switch_to_main_tab(context):
    """
    Switch back to the main application's browser tab.
    """
    context.driver.switch_to.window(context.tabs[0])
    logging.info("Switched back to the main tab.")


@when("the user extracts a name and performs \"Ask For Help\" actions")
def step_extract_name_and_ask_help(context):
    """
    Extract a name from the main application and perform 'Ask For Help' actions.
    """
    context.extracted_name = verify_names(context.driver)
    logging.info(f"Extracted name: {context.extracted_name}")

    ask_for_help_xpath = "//a[normalize-space()='Ask For Help']"
    ask_for_help_selected = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ask_for_help_xpath)),
        "Ask For Help button not clickable."
    )
    ask_for_help_selected.click()
    ask_for_help(context.driver)
    logging.info("Completed 'Ask For Help' actions.")


@then("the user verifies the extracted name in the admin tab")
def step_verify_name_in_admin_tab(context):
    """
    Verify the extracted name in the admin application's browser tab.
    """
    context.driver.switch_to.window(context.tabs[1])
    logging.info("Switched to the admin tab.")
    verify_name_admin_notification(context.driver, context.extracted_name)
    logging.info("Name verification completed in the admin tab.")


@then("the workflow execution is completed")
def step_workflow_completed(context):
    """
    Complete the workflow execution and quit the browser.
    """
    logging.info("Workflow execution completed.")
    context.driver.quit()