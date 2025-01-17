import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import login_to_application   
from utils.locators import click_random_emotion, click_random_slider, compass_dashboard_audio
from pages.login import login_to_application   
from utils.audio import first_audio_homepage   
from utils.locators_for_grade_5 import select_audio_emotions, select_random_mood, grade_5_submit, sub_mood_submit, execute_random_action
from utils.locators import ask_for_help


def get_driver():
    """ Initializes and returns a Chrome WebDriver instance with predefined options. """
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')  # Run in headless mode for CI/CD environments
    # chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    # chrome_options.add_argument('--no-sandbox')  # Disable sandbox for Docker environments
    # chrome_options.add_argument('--disable-dev-shm-usage')  # Handle limited resource issues
    # chrome_options.add_argument('--remote-debugging-port=9222')  # Debugging support
    # chrome_options.add_argument('--mute-audio')  # Mute audio for automated testing
    # chrome_options.add_argument('--use-gl=swiftshader')  # Use SwiftShader for rendering
    # chrome_options.add_argument('--disable-software-rasterizer')  # Disable software rasterization
    # chrome_options.add_argument("--disable-setuid-sandbox")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

@given('Student is on login page for grade 5 student')
def step_impl(context):
    context.driver = get_driver()
    context.driver.maximize_window()
    # Step 1: Login
    login_to_application(context.driver)
    time.sleep(5)
    
@when('Student clicks on compass dashboard audio button')
def step_impl(context):
    # Step 2: Interact with Compass Dashboard Audio
    compass_dashboard_audio(context.driver)

@when('Student click on audio button for mood')
def step_impl(context): 
    #Step 3 : Click on Audio Button 
    first_audio_homepage(context.driver)

@when('Student select any mood emotion randomly')
def step_impl(context):
    # Step 4: Select a Random Emotion
    click_random_emotion(context.driver)

@when('Student select focused slider randomly')
def step_impl(context):
    # Step 5: Interact with a Random Slider
    click_random_slider(context.driver)
    
@when('Student click on submit button to submit mood')
def step_impl(context):
    # Step 6: Click on Submit Button
    grade_5_submit(context.driver)
    
@then('Student can select sub mood randomly')
def step_impl(context):  
    # Step 7: Select Sub mood
    select_random_mood(context.driver)
    
@then('Student clicks on sub mood audio')
def step_impl(context):
    # Step 8: Click on submood audio 
    select_audio_emotions(context.driver)
    
@then('Student click on submit button of sub mood selection')
def step_impl(context):
    # Step 9: Click on submood submit button
    sub_mood_submit(context.driver)
    
@then('Student can fill ask for help pop or close if visible')
def step_impl(context):
    ask_for_help(context.driver)
    
@then('Student can close or submit after mood')
def step_impl(context):
    # Step 10: Aftermood and resources
    execute_random_action(context.driver)
    
    time.sleep(4)
    