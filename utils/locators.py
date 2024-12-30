# utils/locators.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random

def get_emotion_xpath(emotion_name):
    emotions = {
        "happy": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[1]/div/label/img',
        "angry": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
        "meh": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
        "sad": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[4]/div/label/img',
        "excited": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[5]/div/label/img',
        "fearful": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[6]/div/label/img',
    }
    return emotions.get(emotion_name, "Emotion not found!")


def get_slider_dict():
    slider = {
        "1": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[1]/ngx-slider-tooltip-wrapper[2]/div',
        "2": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[2]/ngx-slider-tooltip-wrapper[2]/div',
        "3": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[3]/ngx-slider-tooltip-wrapper[2]/div',
        "4": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[4]/ngx-slider-tooltip-wrapper[2]/div',
        "5": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[5]/ngx-slider-tooltip-wrapper[2]/div',
    }
    return slider

# mood_utils.py

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


def first_next_button(driver):
    """
    Locates and clicks the 'Next' button using XPath.
    """
    first_next_xpath = "//button[normalize-space()='Next']"
    first_next_button = driver.find_element(By.XPATH, first_next_xpath)
    first_next_button.click()


def second_next_button(driver):
    second_next_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]'

    # Locate and click on the 'first_next' emotion
    second_next_element = driver.find_element(By.XPATH, second_next_xpath)
    second_next_element.click()
    time.sleep(1)


def third_next_button(driver):
    audio_second_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'

    # Locate and click on the 'second_next' emotion
    audio_second_next_element = driver.find_element(By.XPATH, audio_second_next_xpath)
    audio_second_next_element.click()
    time.sleep(2)

def fourth_next_button(driver):
    fourth_next_xpath = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/button[2]"

    # Locate and click on the 'third_next' emotion
    fourth_next_element = driver.find_element(By.XPATH, fourth_next_xpath)
    fourth_next_element.click()
    time.sleep(2)

def fifth_next_button(driver):
    fifth_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'

    # Locate and click on the 'fourth_next' emotion
    fifth_next_element = driver.find_element(By.XPATH, fifth_next_xpath)
    fifth_next_element.click()
    time.sleep(2)

def submit_button(driver):
    submit_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/button[2]'

    # Locate and click on the 'submit' emotion
    submit_element = driver.find_element(By.XPATH, submit_xpath)
    submit_element.click()
    time.sleep(4)


def close_button(driver):
    close_xpath = '/html/body/ngb-modal-window/div/div/app-resources-picked-just-for-you/div/div/div/div[1]/div/span'
    # Locate and click on the 'close' emotion
    close_element = driver.find_element(By.XPATH, close_xpath)
    close_element.click()
    time.sleep(4)

def ask_for_help(driver):
    # Define the XPaths for the "Ask For Help" section and buttons
    ask_for_help_xpath_audio = "//h2[normalize-space()='Ask For Help']"
    ask_for_help_xpath_close = "//span[@aria-label='Close']"
    ask_for_help_talk_button = "//button[normalize-space()='I need to talk']"

    # Select randomly between "Close" and "Talk" options
    action_to_perform = random.choice(['close', 'talk'])

    try:
        # Wait for the "Ask For Help" section to be visible
        ask_for_help_audio_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ask_for_help_xpath_audio))
        )

        # Only proceed if the element is visible
        if ask_for_help_audio_element.is_displayed():
            if action_to_perform == 'close':
                # Click on the "Ask For Help" section to open it
                ask_for_help_audio_element.click()
                time.sleep(3)

                # Close the "Ask For Help" section
                ask_for_help_close_element = driver.find_element(By.XPATH, ask_for_help_xpath_close)
                ask_for_help_close_element.click()
                time.sleep(2)
                print("Closed the 'Ask For Help' section.")

            elif action_to_perform == 'talk':
                # Click on the "Talk" button if selected
                ask_for_help_talk_button_element = driver.find_element(By.XPATH, ask_for_help_talk_button)
                ask_for_help_talk_button_element.click()
                time.sleep(2)

                # Define and randomly select checkboxes and emotions
                question_first_yes_checkbox = "//label[normalize-space()='Yes']"
                question_first_no_checkbox = "//label[normalize-space()='No']"
                checkbox_to_select = random.choice([question_first_yes_checkbox, question_first_no_checkbox])

                question_sad = "//label[@for='ans-3']"
                question_angry = "//label[@for='ans-4']"
                question_happy = "//label[@for='ans-5']"
                selected_emotion = random.choice([question_sad, question_angry, question_happy])

                # Select and click the randomly chosen checkbox
                checkbox_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, checkbox_to_select))
                )
                checkbox_element.click()
                time.sleep(1)

                # Select and click the randomly chosen emotion
                emotion_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, selected_emotion))
                )
                emotion_element.click()
                time.sleep(1)

                # Click the "Next" button (if needed)
                question_next = "//button[@class='btn btn-next btn-dark']"
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, question_next))
                )
                next_button.click()
                time.sleep(2)

                print("Selected options and moved to next.")
            
            else:
                print("No valid action performed.")
        else:
            print("Ask For Help section is not visible.")

    except Exception as e:
        print(f"Error: {str(e)}")





