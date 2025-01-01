import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re

def appreciation_audio(driver):
    time.sleep(1)
    audio = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/h2[1]/i[1]"
    driver.find_element(By.XPATH, audio).click()
    

def randomly_select_appreciation(driver):
    appreciation = [
    "div[class='appreciation-row d-flex flex-column'] li:nth-child(1) div:nth-child(1)",
    "div[class='appreciation-row d-flex flex-column'] li:nth-child(2) div:nth-child(1)",
    "div[class='appreciation-row d-flex flex-column'] li:nth-child(3) div:nth-child(1)",
    "div[class='appreciation-row d-flex flex-column'] li:nth-child(4) div:nth-child(1)",
    "div[class='appreciation-row d-flex flex-column'] li:nth-child(5) div:nth-child(1)",
    "div[class='appreciation-row d-flex flex-column'] li:nth-child(6) div:nth-child(1)",
    "li:nth-child(7) div:nth-child(1)",
    "li:nth-child(8) div:nth-child(1)",
    "ul.d-flex.flex-wrap.icon-smile.icon-appreciation li",
    ]

    selected_appreciation = random.choice(appreciation)
   

    try:
        selected_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selected_appreciation))
        )
        selected_element.click()
        time.sleep(1)
        element = driver.find_element(By.CSS_SELECTOR, selected_appreciation)
        test_appreciation = element.text
        print(f"Trying to select: {repr(test_appreciation)}")
        return selected_appreciation, test_appreciation
    except TimeoutException as e:
        print(f"TimeoutException: Could not find the element. {e}")
        raise
    

def submit(driver):

    submit_button = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/div[1]/button[1]"
    driver.find_element(By.XPATH, submit_button).click()
    time.sleep(2)

def scrollPage(driver):
    main_content_element = driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[3]/form/div/button")

    # Scroll the element into view if it's not visible
    driver.execute_script("arguments[0].scrollIntoView(true);", main_content_element)
    time.sleep(1)

    # Now, scroll the element using its scrollTop property (for vertical scrolling)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", main_content_element)
    time.sleep(1)

    # Alternatively, scroll the element by a certain number of pixels
    driver.execute_script("arguments[0].scrollTop += 500", main_content_element)  # Scroll down 500px
    time.sleep(1)

    # Check if the element is scrollable
    scroll_top = driver.execute_script("return arguments[0].scrollTop;", main_content_element)
    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", main_content_element)
    print(f"Scroll Top: {scroll_top}, Scroll Height: {scroll_height}")


def your_journey(driver):
    time.sleep(2)
    your_journey_xpath = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-sidebar[1]/aside[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[5]/a[1]"
    select_your_journey = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, your_journey_xpath))
        )
    select_your_journey.click()
    
    
    appreciation_log_xpath = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-stats[1]/section[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]"
    select_appreciation_log = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, appreciation_log_xpath))
        )
    select_appreciation_log.click()
    


def check_appreciation_log(driver, test_appreciation):
    verify_appreciation_log = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-stats[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]"

    try:
        check_selected_appreciation_log = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, verify_appreciation_log))
        )
        appreciation_log_text = check_selected_appreciation_log.text.strip()

        # Remove unwanted dynamic text (e.g., timestamp or 'Just now')
        clean_appreciation_log_text = re.sub(r'\n.*$', '', appreciation_log_text).strip()

        # Normalize both strings by removing newlines and converting to lowercase
        found_text = clean_appreciation_log_text.replace("\n", "").strip().lower()
        expected_text = test_appreciation.replace("\n", "").strip().lower()
        
        print(f"Trying to select: {repr(clean_appreciation_log_text)}")

        # Check if the found text matches or is a part of the expected text
        if found_text in expected_text:
            print("Log verification successful. The found text is part of the expected text.")
            time.sleep(5)
        else:
            print(f"Log verification failed. Found: {repr(found_text)}, Expected: {repr(expected_text)}")
    except TimeoutException as e:
        print(f"TimeoutException: Could not find the appreciation log element. {e}")
        raise
