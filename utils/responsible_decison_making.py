import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def select_responsible_decision_making(driver):
    responsible_decision_making = {
        "1": '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[1]/div[1]/input[1]',
        "2": '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[2]/div[1]/input[1]',
        "3": '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[3]/div[1]/input[1]',
    }

    responsible_decision_making_audio = {
        "audio1": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[1]/i[1]",
        "audio2": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[2]/i[1]",
        "audio3": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/ul[1]/li[3]/i[1]",
    }

    # Select a random emotion
    random_responsible_decision_making = random.choice(list(responsible_decision_making.values()))

    # Locate and click on the randomly selected emotion
    responsible_decision_making_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, random_responsible_decision_making)))
    responsible_decision_making_element.click()

    time.sleep(2)

    # Check which option was selected and trigger the corresponding audio
    if random_responsible_decision_making == responsible_decision_making["1"]:
        audio_element = driver.find_element(By.XPATH, responsible_decision_making_audio["audio1"])
        audio_element.click()
    elif random_responsible_decision_making == responsible_decision_making["2"]:
        audio_element = driver.find_element(By.XPATH, responsible_decision_making_audio["audio2"])
        audio_element.click()
    elif random_responsible_decision_making == responsible_decision_making["3"]:
        audio_element = driver.find_element(By.XPATH, responsible_decision_making_audio["audio3"])
        audio_element.click()

    time.sleep(9)
