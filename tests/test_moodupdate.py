import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from dotenv import load_dotenv
import os
from utils.locators import get_emotion_xpath, get_slider_dict, get_mood_dict
from utils.audio import select_audio_emotions
from utils.responsible_decison_making import select_responsible_decision_making
from utils.self_management import handle_self_management
from utils.social_awareness import select_social_awareness_option
from utils.emotions_function import perform_actions
from utils.loginfun import test_logindetails


@pytest.fixture(scope="module")
def setup_browser():
    load_dotenv()

    # Get login details
    url = os.getenv("URL")
    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    yield driver  # Provide the driver instance to tests

    # Teardown: Close the browser
    driver.quit()


# Flow 1: Mood Reporting Before
def test_mood_before(setup_browser):
    driver = setup_browser

    # Login function to login
    test_logindetails(driver)

    # Compass Dashboard
    compass_dashboard_audio_xpath = "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[1]/i[2]"
    compass_dashboard_audio_element = driver.find_element(By.XPATH, compass_dashboard_audio_xpath)
    compass_dashboard_audio_element.click()

    # Assert that the click was successful (e.g., the next element appears)
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//button[normalize-space()='Next']"), "Compass dashboard audio interaction failed"

    # Randomly select an emotion
    emotion_names = ["happy", "angry", "meh", "sad", "excited", "fearful"]
    random_emotion = random.choice(emotion_names)
    emotion_xpath = get_emotion_xpath(random_emotion)

    if emotion_xpath != "Emotion not found!":
        emotion_element = driver.find_element(By.XPATH, emotion_xpath)
        emotion_element.click()

        # Assert the emotion was clicked
        time.sleep(2)
        assert emotion_element.is_displayed(), f"Failed to select emotion: {random_emotion}"

    # Select a random slider
    slider_dict = get_slider_dict()
    slider_names = list(slider_dict.keys())
    random_slider = random.choice(slider_names)
    slider_xpath = slider_dict.get(random_slider, "slider not found!")

    if slider_xpath != "slider not found!":
        slider_element = driver.find_element(By.XPATH, slider_xpath)
        slider_element.click()

        # Assert the slider was clicked
        time.sleep(2)
        assert slider_element.is_displayed(), f"Failed to select slider: {random_slider}"

    # Click on the Next Button
    first_next_xpath = "//button[normalize-space()='Next']"
    first_next_button = driver.find_element(By.XPATH, first_next_xpath)
    first_next_button.click()

    # Select a random sub mood
    mood_dict = get_mood_dict()
    random_mood = random.choice(list(mood_dict.values()))
    random_mood_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, random_mood)))

    # Hover and click the mood
    actions = ActionChains(driver)
    actions.move_to_element(random_mood_element).perform()
    time.sleep(5)

    try:
        random_mood_element.click()
    except Exception as e:
        driver.execute_script("arguments[0].click();", random_mood_element)

    # Assert the mood was selected
    assert random_mood_element.is_displayed(), "Failed to select a mood"

    # Perform audio emotions, decision making, self-management, social awareness, and submit actions
    select_audio_emotions(driver)

    # Select the 'first_next' emotion
    audio_first_next_xpath = "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]"
    audio_first_next_element = driver.find_element(By.XPATH, audio_first_next_xpath)
    audio_first_next_element.click()

    time.sleep(2)

    # Call the function
    select_responsible_decision_making(driver)

    # Select the 'second_next' emotion
    audio_second_next_xpath = "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]"
    audio_second_next_element = driver.find_element(By.XPATH, audio_second_next_xpath)
    audio_second_next_element.click()
    time.sleep(2)

    # Call the function
    handle_self_management(driver)

    # Select the 'third_next' emotion
    audio_third_next_xpath = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/button[2]"
    audio_third_next_element = driver.find_element(By.XPATH, audio_third_next_xpath)
    audio_third_next_element.click()

    # Call the function
    select_social_awareness_option(driver)

    # Select the 'fourth_next' emotion
    audio_fourth_next_xpath = "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]"
    audio_fourth_next_element = driver.find_element(By.XPATH, audio_fourth_next_xpath)
    audio_fourth_next_element.click()
    time.sleep(2)

    # Call the function that performs all actions
    perform_actions(driver)

    # Select the 'submit' emotion
    audio_submit_xpath = "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/button[2]"
    audio_submit_element = driver.find_element(By.XPATH, audio_submit_xpath)
    audio_submit_element.click()
    
    # Assert the Message on the Resource Picked for you pop up
    resourcepickedup_xpath = "/html/body/ngb-modal-window/div/div/app-resources-picked-just-for-you/div/div/div/div[1]/div/h2"
    resourcepickedup_assert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, resourcepickedup_xpath))
    )
    assert resourcepickedup_assert.text == "Resources Picked Just for You" , "Text does not match!!"
    audio_icon_resource_picked_for_you_xpath = "/html/body/ngb-modal-window/div/div/app-resources-picked-just-for-you/div/div/div/div[1]/div/h2/i"
    audio_icon_resource_picked_for_you_click = driver.find_element(By.XPATH, audio_icon_resource_picked_for_you_xpath)
    audio_icon_resource_picked_for_you_click.click()
    
    

    # time.sleep(4)

    # # Select the 'close' emotion
    # audio_close_xpath = "/html/body/ngb-modal-window/div/div/app-resources-picked-just-for-you/div/div/div/div[1]/div/span"
    # audio_close_element = driver.find_element(By.XPATH, audio_close_xpath)
    # audio_close_element.click()

    # time.sleep(4)

    # # Assert the form was submitted
    # time.sleep(4)
    # assert "success" in driver.page_source or driver.title != "Submit", "Final submit failed"


# Flow 2: Mood Reporting with After Mood
def test_mood_after(setup_browser):
    driver = setup_browser
    # Call mood reporting before
    time.sleep(5)
    test_mood_before(driver)
