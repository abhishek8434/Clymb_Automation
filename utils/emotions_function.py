
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Define constants for slider positions and audio buttons
SLIDER_POSITIONS = [0, 214, 428, 643]
AUDIO_BUTTON_XPATHS = {
    "communicate": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/button',
    "works_together": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/button',
    "ask_for_help": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/button',
    "ignore_peer_pressure": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/button'
}

# Function to move the slider and click the audio button
def move_slider_and_click_audio(driver, slider_xpath, audio_button_xpath):
    # Find the slider element
    slider_element = driver.find_element(By.XPATH, slider_xpath)

    # Create ActionChains object to drag the slider
    actions = ActionChains(driver)

    # Get current position (left property) of the slider
    current_left = int(slider_element.value_of_css_property('left').replace('px', ''))

    # Choose a random target position
    random_target_position = random.choice(SLIDER_POSITIONS)

    # Calculate the distance to move the slider based on the target position
    move_by = random_target_position - current_left

    # Perform dragging action
    actions.click_and_hold(slider_element).move_by_offset(move_by, 0).release().perform()

    # Click the audio button
    audio_button = driver.find_element(By.XPATH, audio_button_xpath)
    audio_button.click()

    # Sleep for a brief moment to ensure the actions are completed
    time.sleep(2)

def relationship_skills(driver):
    # Define XPaths for different actions
    communicate_xpaths = [
        "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
        # Add other XPaths for communicate here if needed
    ]
    works_together_xpaths = [
        "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
        # Add other XPaths for works_together here if needed
    ]
    ask_for_help_xpaths = [
        "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
        # Add other XPaths for ask_for_help here if needed
    ]
    ignore_peer_pressure_xpaths = [
        "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
        # Add other XPaths for ignore_peer_pressure here if needed
    ]

    # Select random slider XPaths for each action
    random_communicate_xpath = random.choice(communicate_xpaths)
    random_works_together_xpath = random.choice(works_together_xpaths)
    random_ask_for_help_xpath = random.choice(ask_for_help_xpaths)
    random_ignore_peer_pressure_xpath = random.choice(ignore_peer_pressure_xpaths)

    # Perform actions for 'communicate'
    move_slider_and_click_audio(driver, random_communicate_xpath, AUDIO_BUTTON_XPATHS["communicate"])

    # Perform actions for 'works_together'
    move_slider_and_click_audio(driver, random_works_together_xpath, AUDIO_BUTTON_XPATHS["works_together"])

    # Perform actions for 'ask_for_help'
    move_slider_and_click_audio(driver, random_ask_for_help_xpath, AUDIO_BUTTON_XPATHS["ask_for_help"])

    # Perform actions for 'ignore_peer_pressure'
    move_slider_and_click_audio(driver, random_ignore_peer_pressure_xpath, AUDIO_BUTTON_XPATHS["ignore_peer_pressure"])

