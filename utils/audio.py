from selenium.webdriver.common.by import By
import time

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

