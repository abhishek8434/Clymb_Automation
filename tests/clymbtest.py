from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from dotenv import load_dotenv
import os
from utils.locators import get_emotion_xpath, get_slider_dict, get_mood_dict  # Import the function
from utils.audio import select_audio_emotions
from utils.responsible_decison_making import select_responsible_decision_making
from utils.self_management import handle_self_management
from utils.social_awareness import select_social_awareness_option
from utils.emotions_function import perform_actions

load_dotenv()


# Get login details
url = os.getenv("BASE_URL")
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Initialize WebDriver using Chrome
driver = webdriver.Chrome()  # No need to specify executable_path; it's handled by chromedriver-py
driver.maximize_window()

# Open a webpage
driver.get(url)

# Wait for the page to load completely
time.sleep(2)

# Locate the email input field and password input field by their 'name' or 'id' attributes
email_field = driver.find_element(By.ID, "email")  # Change to correct locator if needed
password_field = driver.find_element(By.ID, "password")  # Change to correct locator if needed

# Locate the login button by its 'type' or 'id'
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust if needed

# Enter the login credentials
email_field.send_keys(username)  # Replace with the actual email
password_field.send_keys(password)  # Replace with the actual password

# Submit the form
login_button.click()

# Wait for a successful login (you can adjust this part to wait for specific elements on the dashboard or homepage)
time.sleep(5)

# Select the 'COMPASS DASHBOARD'
compass_dashboard_audio_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[1]/i[2]'

# Locate and click on the 'COMPASS DASHBOARD' audio
compass_dashboard_audio_element = driver.find_element(By.XPATH, compass_dashboard_audio_xpath)
compass_dashboard_audio_element.click()

# List of possible emotions to click
emotion_names = ["happy", "angry", "meh", "sad", "excited", "fearful"]

# Select a random emotion from the list
random_emotion = random.choice(emotion_names)

# Get the XPath for the randomly selected emotion using the function
emotion_xpath = get_emotion_xpath(random_emotion)

# Locate and click on the randomly selected emotion
if emotion_xpath != "Emotion not found!":
    emotion_element = driver.find_element(By.XPATH, emotion_xpath)
    emotion_element.click()

# Wait for a moment after clicking
time.sleep(2)


# List of possible emotions to click
slider_names = ["1", "2", "3", "4", "5"]

# Select a random slider from the list
random_slider = random.choice(slider_names)

# Get the XPath for the randomly selected slider using the function
slider_dict = get_slider_dict()
slider_xpath = slider_dict.get(random_slider, "slider not found!")

# Locate and click on the randomly selected slider
if slider_xpath != "slider not found!":
    slider_element = driver.find_element(By.XPATH, slider_xpath)
    slider_element.click()

# Wait for a moment after clicking
time.sleep(2)


first_next_xpath = "//button[normalize-space()='Next']"

first_next_button = driver.find_element(By.XPATH, first_next_xpath)
first_next_button.click()

# Wait for a moment after clicking
time.sleep(2)

# Get the mood dictionary using the function
mood_dict = get_mood_dict()

# Select a random mood
random_mood = random.choice(list(mood_dict.values()))

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

# Wait a bit before closing
time.sleep(2)

# # Select the 'tile audio
select_audio_emotions(driver)

time.sleep(2)

# Select the 'first_next' emotion
audio_first_next_xpath = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]'

# Locate and click on the 'first_next' emotion
audio_first_next_element = driver.find_element(By.XPATH, audio_first_next_xpath)
audio_first_next_element.click()

time.sleep(2)

# Call the function
select_responsible_decision_making(driver)

# Select the 'second_next' emotion
audio_second_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'

# Locate and click on the 'second_next' emotion
audio_second_next_element = driver.find_element(By.XPATH, audio_second_next_xpath)
audio_second_next_element.click()
time.sleep(2)

# Call the function
handle_self_management(driver)

# Select the 'third_next' emotion
audio_third_next_xpath = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/button[2]"

# Locate and click on the 'third_next' emotion
audio_third_next_element = driver.find_element(By.XPATH, audio_third_next_xpath)
audio_third_next_element.click()

# Call the function
select_social_awareness_option(driver)

# Select the 'fourth_next' emotion
audio_fourth_next_xpath = '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/button[2]'

# Locate and click on the 'fourth_next' emotion
audio_fourth_next_element = driver.find_element(By.XPATH, audio_fourth_next_xpath)
audio_fourth_next_element.click()
time.sleep(2)

# Call the function that performs all actions
perform_actions(driver)

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