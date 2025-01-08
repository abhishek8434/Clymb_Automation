import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import random

def compass_dashboard_audio(driver):
    compass_dashboard_audio_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[1]/i[2]'
    compass_dashboard_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, compass_dashboard_audio_xpath))
    )
    compass_dashboard_element.click()

def click_random_emotion(driver):
    emotions = {
        "happy": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[1]/div/label/img',
        "angry": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
        "meh": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
        "sad": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[4]/div/label/img',
        "excited": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[5]/div/label/img',
        "fearful": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[6]/div/label/img',
    }

    random_emotion = random.choice(list(emotions.keys()))
    emotion_xpath = emotions.get(random_emotion)

    if emotion_xpath:
        emotion_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, emotion_xpath))
        )
        emotion_element.click()
        print(f"Clicked on the '{random_emotion}' emotion.")
    else:
        print("Emotion not found!")

def click_random_slider(driver):
    slider_dict = {
        "1": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[1]/ngx-slider-tooltip-wrapper[2]/div',
        "2": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[2]/ngx-slider-tooltip-wrapper[2]/div',
        "3": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[3]/ngx-slider-tooltip-wrapper[2]/div',
        "4": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[4]/ngx-slider-tooltip-wrapper[2]/div',
        "5": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[5]/ngx-slider-tooltip-wrapper[2]/div',
    }

    random_slider = random.choice(["1", "2", "3", "4", "5"])
    slider_xpath = slider_dict.get(random_slider, None)

    if slider_xpath:
        slider_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, slider_xpath))
        )
        slider_element.click()
    else:
        print("Slider not found!")

def select_random_mood(driver):
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

    random_mood = random.choice(list(mood.values()))
    random_mood_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, random_mood))
    )
    ActionChains(driver).move_to_element(random_mood_element).perform()

    try:
        random_mood_element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", random_mood_element)

def first_next_button(driver):
    first_next_xpath = "//button[normalize-space()='Next']"
    first_next_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, first_next_xpath))
    )
    first_next_button.click()

def second_next_button(driver):
    second_next_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]'
    second_next_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, second_next_xpath))
    )
    second_next_element.click()

def third_next_button(driver):
    audio_second_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'
    audio_second_next_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, audio_second_next_xpath))
    )
    audio_second_next_element.click()

def fourth_next_button(driver):
    fourth_next_xpath = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/button[2]"
    fourth_next_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, fourth_next_xpath))
    )
    fourth_next_element.click()

def fifth_next_button(driver):
    fifth_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'
    fifth_next_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, fifth_next_xpath))
    )
    fifth_next_element.click()

def submit_button(driver):
    submit_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/button[2]'
    submit_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, submit_xpath))
    )
    submit_element.click()

def close_button(driver):
    close_xpath = '/html/body/ngb-modal-window/div/div/app-resources-picked-just-for-you/div/div/div/div[1]/div/span'
    close_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, close_xpath))
    )
    close_element.click()

def ask_for_help(driver):
    # Define the XPaths for the "Ask For Help" section and buttons
    ask_for_help_xpath_audio = "//h2[normalize-space()='Ask For Help']"
    ask_for_help_xpath_close = "//span[@aria-label='Close']"
    ask_for_help_talk_button = "//button[normalize-space()='I need to talk']"

    # Select randomly between "Close" and "Talk" options
    action_to_perform = random.choice(['close', 'talk'])

    try:
        # Wait for the "Ask For Help" section to be visible
        ask_for_help_audio_element = WebDriverWait(driver, 20).until(
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
                checkbox_element = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, checkbox_to_select))
                )
                checkbox_element.click()
                time.sleep(1)
                
                # Click the "Next" button (if needed)
                question_next = "//button[@class='btn btn-next btn-dark']"
                next_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, question_next))
                )
                next_button.click()
                time.sleep(2)
                print("Selected options and moved to next.")
                
                # Select and click the randomly chosen emotion
                emotion_element = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, selected_emotion))
                )
                emotion_element.click()
                time.sleep(1)
                
                 # Click the "Next" button (if needed)
                question_submit = "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-ask-for-help[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[4]/div[2]/button[1]"
                submit_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, question_submit))
                )
                submit_button.click()
                time.sleep(2)
                print("Selected options and Submit.")

            else:
                print("No valid action performed.")
        else:
            print("Ask For Help section is not visible.")

    except Exception as e:
        print(f"Error: {str(e)}")





