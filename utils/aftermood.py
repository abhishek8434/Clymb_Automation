import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import ask_for_help

# Main function to execute one of the above functions randomly
def execute_random_action(driver):
    # List of functions
    actions = [close_button, aftermood]
    
    # Select a function randomly
    selected_action = random.choice(actions)
    
    # Execute the randomly selected function
    selected_action(driver)

# Function to handle aftermood process
def aftermood(driver):

    resource1 = "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-resources-picked-just-for-you[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"
    resource2 = "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-resources-picked-just-for-you[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]"
    resource3 = "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-resources-picked-just-for-you[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]"

    random_resource = random.choice([resource1, resource2, resource3])

    # Select and click the randomly chosen resource
    resource_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, random_resource))
    )
    resource_element.click()
    time.sleep(3)

    resource_close = "//span[@aria-label='Close']"
    resource_close_element = driver.find_element(By.XPATH, resource_close)
    resource_close_element.click()
    time.sleep(4)

    # Step 1: Randomly select an emotion
    emotions = list(get_emotion_xpath_aftermood(None).keys())  # Fetch all emotion keys
    selected_emotion = random.choice(emotions)
    emotion_xpath = get_emotion_xpath_aftermood(selected_emotion)
    
    emotion_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, emotion_xpath))
    )
    emotion_element.click()
    time.sleep(1)
    
    # Step 2: Randomly select a slider value
    slider_dict = get_slider_dict_aftermood()
    selected_slider_key = random.choice(list(slider_dict.keys()))
    slider_xpath = slider_dict[selected_slider_key]
    
    slider_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, slider_xpath))
    )
    slider_element.click()
    time.sleep(1)

    next_button = "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-after[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]"
    next_button_element = driver.find_element(By.XPATH, next_button)
    next_button_element.click()
    time.sleep(2)

   
    # Step 3: Randomly select a mood
    mood_dict = get_mood_dict()
    selected_mood = random.choice(list(mood_dict.keys()))
    mood_xpath = mood_dict[selected_mood]
    
    mood_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, mood_xpath))
    )
    mood_element.click()
    time.sleep(1)

    # Step 4: Submit aftermood
    aftermood_submit_button(driver)

# Function to handle closing the modal or overlay
def close_button(driver):
    try:
        close_button_xpath = "/html/body/ngb-modal-window/div/div/div/button"  # Update this XPath as needed
        close_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, close_button_xpath))
        )
        close_element.click()
        print("Modal closed successfully.")
    except Exception as e:
        print(f"Failed to close modal: {e}")

# Function to fetch emotion XPaths
def get_emotion_xpath_aftermood(aftermood_emotion_name):
    emotions = {
        "happy": '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-after[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/label[1]/img[1]',
        "angry": '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-after[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/label[1]/img[1]',
        "meh": '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-after[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/div[1]/label[1]/img[1]',
        "sad": '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-after[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/div[1]/label[1]/img[1]',
        "excited": '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-after[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/div[1]/label[1]/img[1]',
        "fearful": '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-after[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[6]/div[1]/label[1]/img[1]',
    }
    return emotions.get(aftermood_emotion_name, emotions)

# Function to fetch slider XPaths
def get_slider_dict_aftermood():
    slider = {
        "1": '/html/body/ngb-modal-window/div/div/app-after/div/div/div/div[1]/div/div[2]/div/ngx-slider/span[12]/span[1]/ngx-slider-tooltip-wrapper[2]/div',
        "2": '/html/body/ngb-modal-window/div/div/app-after/div/div/div/div[1]/div/div[2]/div/ngx-slider/span[12]/span[2]/ngx-slider-tooltip-wrapper[2]/div',
        "3": '/html/body/ngb-modal-window/div/div/app-after/div/div/div/div[1]/div/div[2]/div/ngx-slider/span[12]/span[3]/ngx-slider-tooltip-wrapper[2]/div',
        "4": '/html/body/ngb-modal-window/div/div/app-after/div/div/div/div[1]/div/div[2]/div/ngx-slider/span[12]/span[4]/ngx-slider-tooltip-wrapper[2]/div',
        "5": '/html/body/ngb-modal-window/div/div/app-after/div/div/div/div[1]/div/div[2]/div/ngx-slider/span[12]/span[5]/ngx-slider-tooltip-wrapper[2]/div',
    }
    return slider

# Function to fetch mood XPaths
def get_mood_dict():
    mood = {
        "mood1": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][1]/*[name()='path'][3]",
        "mood2": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][1]/*[name()='path'][4]",
        "mood3": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][2]/*[name()='path'][3]",
        "mood4": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][2]/*[name()='path'][4]",
        "mood5": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][3]/*[name()='path'][3]",
        "mood6": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][3]/*[name()='path'][4]",
        "mood7": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][4]/*[name()='path'][3]",
        "mood8": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][4]/*[name()='path'][4]",
    }
    return mood

# Function to handle submit and random selection of post action
def aftermood_submit_button(driver):
    submit_button = "/html/body/ngb-modal-window/div/div/app-emotion-wheel/div/div/div/div[1]/div/div/div[2]/div[2]/button"
    submit_button_element = driver.find_element(By.XPATH, submit_button)
    submit_button_element.click()
    time.sleep(2)

    post_cancel = "/html/body/ngb-modal-window/div/div/app-share-post/div/div/div/div[1]/div/div/div[1]/div/form/div[2]/button[2]"
    post_submit = "/html/body/ngb-modal-window/div/div/app-share-post/div/div/div/div[1]/div/div/div[1]/div/form/div[2]/button[1]"

    random_cancel_submit = random.choice([post_cancel, post_submit])

    # Select and click the randomly chosen resource
    submit_cancel_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, random_cancel_submit))
    )
    submit_cancel_element.click()
    time.sleep(1)

    ask_for_help(driver)

    time.sleep(2)



