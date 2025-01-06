import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login import login_to_application
from utils.locators import ask_for_help
from pages.admin_login import login_to_application_admin
from utils.verify_ask_for_help_locator import verify_names, verify_name_admin_notification


@pytest.fixture(scope="module")
def driver():
    """Initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_workflow(driver):
    """Execute the full workflow with both tabs opened simultaneously."""

    # Step 1: Perform login actions in the first tab (Main application)
    login_to_application(driver)  # Executes all actions for login on the first tab
    print("Main application login completed.")
    WebDriverWait(driver, 10).until(EC.url_changes)  # Wait for the URL to change after login

    # Step 2: Open the second tab and perform admin login actions
    driver.execute_script("window.open('');")  # Open a new tab
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    login_to_application_admin(driver)  # Executes all actions for admin login on the second tab
    print("Admin application login completed.")
    WebDriverWait(driver, 10).until(EC.url_changes)  # Wait for the URL to change after admin login

    # Step 3: Switch back to the first tab
    driver.switch_to.window(tabs[0])
    print("Switched back to the first tab.")

    # Fetch the extracted name
    extracted_name = verify_names(driver)
    print(f"Extracted name: {extracted_name}")

    # Perform additional actions in the first tab
    ask_for_help_xpath = "//a[normalize-space()='Ask For Help']"
    ask_for_help_selected = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ask_for_help_xpath))
    )
    ask_for_help_selected.click()
    ask_for_help(driver)  # Perform the "Ask For Help" actions
    print("Completed actions in the first tab.")

    # Step 4: Switch to the admin tab to verify the extracted name
    driver.switch_to.window(tabs[1])
    print("Switched to the admin tab.")

    verify_name_admin_notification(driver, extracted_name)  # Verify the name in the admin tab
    print("Name verification completed in the admin tab.")

    # Optional: Perform further actions or validations in the admin tab if needed
    print("Workflow execution completed.")
