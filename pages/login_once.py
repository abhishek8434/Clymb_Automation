import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login_to_application_loop(driver):
    """Log in to the application using the provided WebDriver instance."""
    # Define login credentials from environment variables
    login_details = [
        {"username": os.getenv("EMAIL"), "password": os.getenv("PASSWORD")},
        {"username": os.getenv("EMAIL1"), "password": os.getenv("PASSWORD1")},
        {"username": os.getenv("EMAIL2"), "password": os.getenv("PASSWORD2")},
        {"username": os.getenv("EMAIL3"), "password": os.getenv("PASSWORD3")},
        {"username": os.getenv("EMAIL4"), "password": os.getenv("PASSWORD4")},
        {"username": os.getenv("EMAIL5"), "password": os.getenv("PASSWORD5")},
        {"username": os.getenv("EMAIL6"), "password": os.getenv("PASSWORD6")},
        {"username": os.getenv("EMAIL7"), "password": os.getenv("PASSWORD7")},
        {"username": os.getenv("EMAIL8"), "password": os.getenv("PASSWORD8")},
        {"username": os.getenv("EMAIL9"), "password": os.getenv("PASSWORD9")},
    ]

    # URL of the login page
    login_url = os.getenv("LIVE_URL")
    print(login_url)

    # Loop over the credentials and log in
    for creds in login_details:
        if creds["username"] and creds["password"]:
            driver.get(login_url)
            
            try:
                # Step 1: Enter email
                email_field = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'email'))
                )
                email_field.send_keys(creds["username"])

                # Step 2: Enter password
                password_field = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'password'))
                )  
                password_field.send_keys(creds["password"])

                # Step 3: Click login button
                login_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
                )
                login_button.click()

                time.sleep(5)  # Wait for login to process
                print(f"Login successful for {creds['username']}")

            except Exception as e:
                print(f"Error logging in for {creds['username']}: {e}")
