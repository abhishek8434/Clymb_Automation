import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from selenium import webdriver
from pages.login import login_to_application
from utils.locators import change_language    
from utils.appreciation import randomly_select_appreciation, submit, appreciation_audio, scrollPage
from utils.audio import second_audio_homepage
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


logging.basicConfig(level=logging.INFO)


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

# Positive Flow

@given('I am logged into the application1')
def step_login(context):
   
    context.driver = get_driver()
    context.driver.maximize_window()
    login_to_application(context.driver)
    time.sleep(5)
    change_language(context.driver)

@when('I scroll to the end of the page1')
def step_scroll_page(context):
    scrollPage(context.driver)


@when('I click on the appreciation audio button1')
def step_click_appreciation_audio(context):
    appreciation_audio(context.driver)


@when('I click on the appreciation log audio button1')
def step_click_log_audio(context):
    second_audio_homepage(context.driver)


@when('I select an appreciation randomly1')
def step_select_appreciation(context):
    randomly_select_appreciation(context.driver)


@then('I submit the appreciation1')
def step_submit_appreciation(context):
    submit(context.driver)
    context.driver.quit()




