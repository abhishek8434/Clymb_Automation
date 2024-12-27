import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_social_awareness_option(driver):
    social_awareness = {
        "1": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[1]",
        "2": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[2]",
        "3": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[3]",
        "4": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[4]",
        "5": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ngx-slider[1]/span[12]/span[5]",
    }

    social_awareness_audio = {
        "audio1": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li[1]/button[1]",
        "audio2": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li[2]/button[1]",
        "audio3": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li[3]/button[1]",
        "audio4": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li[4]/button[1]",
        "audio5": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li[5]/button[1]",
    }

    # Select a random emotion
    random_social_awareness = random.choice(list(social_awareness.values()))

    # Wait for the element to be clickable
    social_awareness_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, random_social_awareness))
    )

    # Hover over the element
    actions = ActionChains(driver)
    actions.move_to_element(social_awareness_element).perform()

    # Wait and attempt to click the element
    time.sleep(2)
    try:
        social_awareness_element.click()
    except Exception as e:
        print(f"Error clicking element: {str(e)}")
        driver.execute_script("arguments[0].click();", social_awareness_element)

    # Trigger corresponding audio
    for key, value in social_awareness.items():
        if random_social_awareness == value:
            audio_element = driver.find_element(By.XPATH, social_awareness_audio[f"audio{key}"])
            audio_element.click()
            break

    time.sleep(4)
