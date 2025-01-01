from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_audio_emotions(driver):
    # Define the XPaths for each element to be clicked
    xpaths = {
        "audio_title": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h4[1]/i[1]",
        "audio_look_like": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h5[1]/i[1]",
        "audio_first_description": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/i[1]",
        "audio_second_description": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/i[1]",
        "audio_third_description": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/i[1]",
        "audio_feel_like": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h5[2]/i[1]",
        "audio_first_description_feels": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[1]/i[1]",
        "audio_second_description_feels": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[2]/i[1]",
        "audio_third_description_feels": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[3]/i[1]",
    }

    # Loop through each element's XPath and click it with a small delay
    for key, xpath in xpaths.items():
        try:
            # Find the element by XPath
            element = driver.find_element(By.XPATH, xpath)
            # Click the element
            element.click()
            # Wait for 2 seconds before the next action
            time.sleep(2)
            print(f"Clicked on {key}")
        except Exception as e:
            print(f"Failed to click on {key}: {e}")
            
def first_audio_homepage(driver):
    first_audio_homepage_xpath = "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div/div/figure/img"
    first_audio_homepage_selected = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_audio_homepage_xpath))
        )
    first_audio = first_audio_homepage_selected.click()

def second_audio_homepage(driver):
    time.sleep(2)
    second_audio_homepage_xpath = "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[3]/form/div/div/div/div/figure/img"
    second_audio_homepage_selected = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, second_audio_homepage_xpath))
        )
    second_audio = second_audio_homepage_selected.click()