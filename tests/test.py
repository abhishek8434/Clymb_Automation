from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Initialize WebDriver using Chrome
driver = webdriver.Chrome()  # No need to specify executable_path; it's handled by chromedriver-py
driver.maximize_window()
# Open a webpage
driver.get("https://clymbstudent.evdpl.com/account/login")

# Wait for the page to load completely
time.sleep(2)

# Locate the email input field and password input field by their 'name' or 'id' attributes
email_field = driver.find_element(By.ID, "email")  # Change to correct locator if needed
password_field = driver.find_element(By.ID, "password")  # Change to correct locator if needed

# Locate the login button by its 'type' or 'id'
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust if needed

# Enter the login credentials
email_field.send_keys("bonney12@yopmail.com")  # Replace with the actual email
password_field.send_keys("Test@123")  # Replace with the actual password

# Submit the form
login_button.click()

# Wait for a successful login (you can adjust this part to wait for specific elements on the dashboard or homepage)
time.sleep(5)

# Optionally, take a screenshot after login
driver.save_screenshot("login_success.png")

# # Select the 'happy' emotion
# happy_emotion_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[1]/div/label/img'

# # Locate and click on the 'happy' emotion
# happy_emotion_element = driver.find_element(By.XPATH, happy_emotion_xpath)
# happy_emotion_element.click()


# List of possible emotions to click
emotions = {
    "happy": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[1]/div/label/img',
    "angry": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
    "meh": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
    "sad": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[4]/div/label/img',
    "excited": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[5]/div/label/img',
    "fearful": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[6]/div/label/img'
}

# Select a random emotion
random_emotion = random.choice(list(emotions.values()))

# Locate and click on the randomly selected emotion
emotion_element = driver.find_element(By.XPATH, random_emotion)
emotion_element.click()

# Wait for a moment after clicking
time.sleep(2)

# Optionally, take a screenshot after the emotion is selected
driver.save_screenshot("emotion_selected.png")

slider = {
    "1": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[1]/ngx-slider-tooltip-wrapper[2]/div',
    "2": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[2]/ngx-slider-tooltip-wrapper[2]/div',
    "3": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[3]/ngx-slider-tooltip-wrapper[2]/div',
    "4": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[4]/ngx-slider-tooltip-wrapper[2]/div',
    "5": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[5]/ngx-slider-tooltip-wrapper[2]/div',
    
}

# Select a random emotion
random_slider = random.choice(list(slider.values()))

# Locate and click on the randomly selected emotion
slider_element = driver.find_element(By.XPATH, random_slider)
slider_element.click()

first_next_xpath = "//button[normalize-space()='Next']"

first_next_button = driver.find_element(By.XPATH, first_next_xpath)
first_next_button.click()

# Wait for a moment after clicking
time.sleep(2)


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


# Select a random emotion
random_mood = random.choice(list(mood.values()))


# Wait for the element to be clickable
random_mood_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, random_mood))
)

# Create an instance of ActionChains
actions = ActionChains(driver)

# Hover over the element
actions.move_to_element(random_mood_element).perform()

# Wait for 1 second after hover
time.sleep(2)

# Attempt to click the element
try:
    random_mood_element.click()
except Exception as e:
    print(f"Error clicking element: {str(e)}")
    # Fallback to JavaScript click if normal click fails
    driver.execute_script("arguments[0].click();", random_mood_element)


time.sleep(1)

# Select the 'tile audio' emotion
audio_title_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h4[1]/i[1]'

# Locate and click on the 'audio_title' emotion
audio_title_element = driver.find_element(By.XPATH, audio_title_xpath)
audio_title_element.click()

time.sleep(2)

# Select the 'look like' emotion
audio_look_like_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h5[1]/i[1]'

# Locate and click on the 'look_like' emotion
audio_look_like_element = driver.find_element(By.XPATH, audio_look_like_xpath)
audio_look_like_element.click()

time.sleep(2)

# Select the 'first_description' emotion
audio_first_description_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/i[1]'

# Locate and click on the 'first_description' emotion
audio_first_description_element = driver.find_element(By.XPATH, audio_first_description_xpath)
audio_first_description_element.click()

time.sleep(2)

# Select the 'second_description' emotion
audio_second_description_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/i[1]'

# Locate and click on the 'second_description' emotion
audio_second_description_element = driver.find_element(By.XPATH, audio_second_description_xpath)
audio_second_description_element.click()

time.sleep(2)

# Select the 'third_description' emotion
audio_third_description_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/i[1]'

# Locate and click on the 'third_description' emotion
audio_third_description_element = driver.find_element(By.XPATH, audio_third_description_xpath)
audio_third_description_element.click()

time.sleep(2)

# Select the 'feel_like' emotion
audio_feel_like_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h5[2]/i[1]'

# Locate and click on the 'feel_like' emotion
audio_feel_like_element = driver.find_element(By.XPATH, audio_feel_like_xpath)
audio_feel_like_element.click()

time.sleep(2)

# Select the 'first_description_feels' emotion
audio_first_description_feels_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[1]/i[1]'

# Locate and click on the 'first_description_feels' emotion
audio_first_description_feels_element = driver.find_element(By.XPATH, audio_first_description_feels_xpath)
audio_first_description_feels_element.click()

time.sleep(2)

# Select the 'second_description_feels' emotion
audio_second_description_feels_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[2]/i[1]'

# Locate and click on the 'second_description_feels' emotion
audio_second_description_feels_element = driver.find_element(By.XPATH, audio_second_description_feels_xpath)
audio_second_description_feels_element.click()

time.sleep(2)

# Select the 'third_description_feels' emotion
audio_third_description_feels_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[3]/i[1]'

# Locate and click on the 'third_description_feels' emotion
audio_third_description_feels_element = driver.find_element(By.XPATH, audio_third_description_feels_xpath)
audio_third_description_feels_element.click()

time.sleep(2)

# Select the 'first_next' emotion
audio_first_next_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]'

# Locate and click on the 'first_next' emotion
audio_first_next_element = driver.find_element(By.XPATH, audio_first_next_xpath)
audio_first_next_element.click()

time.sleep(2)

responsible_decison_making = {
    "1": '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[1]/div[1]/input[1]',
    "2": '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[2]/div[1]/input[1]',
    "3": '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[3]/div[1]/input[1]',
        
}

# Select a random emotion
random_responsible_decison_making = random.choice(list(responsible_decison_making.values()))

# Locate and click on the randomly selected emotion
responsible_decison_making_element = driver.find_element(By.XPATH, random_responsible_decison_making)
responsible_decison_making_element.click()

time.sleep(2)
# Select the 'second_next' emotion
audio_second_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'

# Locate and click on the 'second_next' emotion
audio_second_next_element = driver.find_element(By.XPATH, audio_second_next_xpath)
audio_second_next_element.click()
time.sleep(2)

self_management = {
    "1": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='path'][1]",
    "2": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][2]/*[name()='g'][1]/*[name()='path'][1]",
    "3": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][3]/*[name()='g'][1]/*[name()='path'][1]",
    "4": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][4]/*[name()='g'][1]/*[name()='path'][1]",
    "5": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][5]/*[name()='g'][1]/*[name()='path'][1]",
        
}
# Select a random emotion
random_self_management = random.choice(list(self_management.values()))

# Wait for the element to be clickable
self_management_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, random_self_management))
)

# Create an instance of ActionChains
actions = ActionChains(driver)

# Hover over the element
actions.move_to_element(self_management_element).perform()

# Wait for 1 second after hover
time.sleep(2)

# Attempt to click the element
try:
    self_management_element.click()
except Exception as e:
    print(f"Error clicking element: {str(e)}")
    # Fallback to JavaScript click if normal click fails
    driver.execute_script("arguments[0].click();", self_management_element)

# Wait for 1 second after clicking
time.sleep(1)


# Select the 'third_next' emotion
audio_third_next_xpath = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/button[2]"

# Locate and click on the 'third_next' emotion
audio_third_next_element = driver.find_element(By.XPATH, audio_third_next_xpath)
audio_third_next_element.click()


social_awareness = {
    "1": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[1]",
    "2": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[2]",
    "3": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[3]",
    "4": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[4]",
    "5": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[5]",
        
}

# Select a random emotion
random_social_awareness = random.choice(list(social_awareness.values()))

# Wait for the element to be clickable
social_awareness_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, random_social_awareness))
)

# Create an instance of ActionChains
actions = ActionChains(driver)

# Hover over the element
actions.move_to_element(social_awareness_element).perform()

# Wait for 1 second after hover
time.sleep(2)

# Attempt to click the element
try:
    social_awareness_element.click()
except Exception as e:
    print(f"Error clicking element: {str(e)}")
    # Fallback to JavaScript click if normal click fails
    driver.execute_script("arguments[0].click();", social_awareness_element)

# Wait for 1 second after clicking
time.sleep(1)


# Select the 'fourth_next' emotion
audio_fourth_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'

# Locate and click on the 'fourth_next' emotion
audio_fourth_next_element = driver.find_element(By.XPATH, audio_fourth_next_xpath)
audio_fourth_next_element.click()
time.sleep(2)


time.sleep(2)
communicate = {
    "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
    "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
    "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
    "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",

        
}

# Select a random emotion
random_communicate = random.choice(list(communicate.values()))

# Locate and click on the randomly selected emotion
communicate_element = driver.find_element(By.XPATH, random_communicate)
communicate_element.click()


works_together = {
    "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
    "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
    "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
    "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
    
        
}

# Select a random emotion
random_works_together = random.choice(list(works_together.values()))

# Locate and click on the randomly selected emotion
works_together_element = driver.find_element(By.XPATH, random_works_together)
works_together_element.click()

ask_for_help = {
    "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
    "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
    "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
    "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
        
}

# Select a random emotion
random_ask_for_help = random.choice(list(ask_for_help.values()))

# Locate and click on the randomly selected emotion
ask_for_help_element = driver.find_element(By.XPATH, random_ask_for_help)
ask_for_help_element.click()


ignore_peer_pressure = {
    "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
    "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
    "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
    "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
        
}

# Select a random emotion
random_ignore_peer_pressure = random.choice(list(ignore_peer_pressure.values()))

# Locate and click on the randomly selected emotion
ignore_peer_pressure_element = driver.find_element(By.XPATH, random_ignore_peer_pressure)
ignore_peer_pressure_element.click()


# Select the 'submit' emotion
audio_submit_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/button[2]'

# Locate and click on the 'submit' emotion
audio_submit_element = driver.find_element(By.XPATH, audio_submit_xpath)
audio_submit_element.click()



time.sleep(4)


# Select the 'close' emotion
audio_close_xpath = '/html/body/ngb-modal-window/div/div/app-resources-picked-just-for-you/div/div/div/div[1]/div/span'

# Locate and click on the 'close' emotion
audio_close_element = driver.find_element(By.XPATH, audio_close_xpath)
audio_close_element.click()


time.sleep(4)

# Close the browser
driver.quit()