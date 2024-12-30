import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from utils.locators import get_emotion_xpath, get_slider_dict, get_mood_dict
from utils.locators import first_next_button, second_next_button, third_next_button, fourth_next_button, fifth_next_button, submit_button, close_button
from utils.locators import ask_for_help
from utils.audio import select_audio_emotions
from utils.responsible_decison_making import select_responsible_decision_making
from utils.self_management import handle_self_management
from utils.social_awareness import select_social_awareness_option
from utils.emotions_function import perform_actions
from utils.self_management import handle_self_management

# Load environment variables
load_dotenv()

# Get login details
url = os.getenv("BASE_URL")
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


@pytest.fixture(scope="module")
def driver():
    """Initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_workflow(driver):
    """Execute the full workflow in sequence."""
    driver.get(url)
    time.sleep(2)

    # Step 1: Login
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    email_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)

    # Step 2: Interact with Compass Dashboard Audio
    compass_dashboard_audio_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[1]/i[2]'
    driver.find_element(By.XPATH, compass_dashboard_audio_xpath).click()
    time.sleep(2)

    # Step 3: Select a Random Emotion
    random_emotion = random.choice(["happy", "angry", "meh", "sad", "excited", "fearful"])
    emotion_xpath = get_emotion_xpath(random_emotion)
    if emotion_xpath != "Emotion not found!":
        driver.find_element(By.XPATH, emotion_xpath).click()
        time.sleep(2)

    # Step 4: Interact with a Random Slider
    random_slider = random.choice(["1", "2", "3", "4", "5"])
    slider_xpath = get_slider_dict().get(random_slider, "slider not found!")
    if slider_xpath != "slider not found!":
        driver.find_element(By.XPATH, slider_xpath).click()
        time.sleep(2)

    # Step 5: Click First 'Next' Button
    first_next_button(driver)

    # Step 6: Select a Random Mood
    random_mood = random.choice(list(get_mood_dict().values()))
    random_mood_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, random_mood))
    )
    ActionChains(driver).move_to_element(random_mood_element).perform()
    time.sleep(2)
    try:
        random_mood_element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", random_mood_element)
    time.sleep(2)

    # Step 7: Select Audio Emotions
    select_audio_emotions(driver)

    # Step 8: Click Second 'Next' Button
    second_next_button(driver)

    # Step 9: Check For Ask For Help Popup and will close
    ask_for_help(driver)

    # Step 10: Select Responsible Decision Making
    select_responsible_decision_making(driver)

    # Step 11: Click Third 'Next' Button
    third_next_button(driver)

    # Step 12: Handle Self-Management Actions
    handle_self_management(driver)

    # def test_handle_self_management(driver):
    # # # Ensure the driver is loaded properly and then call the function
    #      handle_self_management(driver)

    # Step 13: Click Fourth 'Next' Button
    fourth_next_button(driver)

    # Step 14: Select Social Awareness Option
    select_social_awareness_option(driver)

    # Step 15: Click Fifth 'Next' Button
    fifth_next_button(driver)

    # Step 16: Perform Custom Actions
    perform_actions(driver)

    # Step 17: Submit the Form
    submit_button(driver)

    # Step 18: Close the Final Modal
    close_button(driver)
    time.sleep(2)
