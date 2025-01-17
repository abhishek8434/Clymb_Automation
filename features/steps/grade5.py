import time
from behave import given, when, then
from utils.locators import click_random_emotion, click_random_slider, compass_dashboard_audio
from pages.login import login_to_application_grade5   
from utils.audio import first_audio_homepage   
from utils.locators_for_grade_5 import select_audio_emotions, select_random_mood, grade_5_submit, sub_mood_submit, execute_random_action
from utils.locators import ask_for_help
from utils.drivers import setup_driver

@given('Student is on login page for grade 5 student')
def step_impl(context):
    context.driver = setup_driver()
    context.driver.maximize_window()
    # Step 1: Login
    login_to_application_grade5(context.driver)
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
    