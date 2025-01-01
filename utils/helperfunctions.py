# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# from dotenv import load_dotenv

# def login(driver):
#     """
#     Perform login using the provided driver, email, and password.

#     Args:
#         driver: Selenium WebDriver instance.
#         email: Email or username for login.
#         password: Password for login.
#         timeout: Maximum wait time for elements to appear (default: 10 seconds).

#     Raises:
#         Exception: If any of the elements required for login are not found.
#     """
#     # def setup_browser():
#     # Load environment variables
#     load_dotenv()

#     # Get login details
#     url = os.getenv("URL")
#     username = os.getenv("EMAIL")
#     password = os.getenv("PASSWORD")

#     # Initialize WebDriver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(url)

#     yield driver  # Provide the driver instance to tests

#     # Teardown: Close the browser
#     driver.quit()
#     try:
#         # Wait for the email field to be visible
#         email_field = WebDriverWait(driver, timeout).until(
#             EC.presence_of_element_located((By.ID, "email"))
#         )
#         password_field = driver.find_element(By.ID, "password")
#         login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

#         # Enter login credentials
#         email_field.send_keys(email)
#         password_field.send_keys(password)

#         # Click the login button
#         login_button.click()

#         # Wait for the login process to complete (adjust condition as per your application)
#         WebDriverWait(driver, timeout).until(
#             EC.url_contains("dashboard")  # Update with a specific condition for your app
#         )
#         print("Login successful.")

#     except Exception as e:
#         print(f"Error during login: {e}")
#         raise
