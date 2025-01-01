import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
        

def appreciation_audio(driver):
    audio = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/h2[1]/i[1]"
    driver.find_element(By.XPATH, audio).click()
    

def randomly_select_appreciation(driver):
    family = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[1]/div[1]/label[1]/img[1]"
    friends = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[2]/div[1]/label[1]/img[1]"
    school = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[3]/div[1]/label[1]/img[1]"
    me = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[4]/div[1]/label[1]/img[1]"
    teacher = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[5]/div[1]/label[1]/img[1]"
    technology = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[6]/div[1]/label[1]/img[1]"
    math = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[7]/div[1]/label[1]/img[1]"
    music = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[8]/div[1]/label[1]/img[1]"
    art = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/fieldset[1]/ul[1]/li[9]/div[1]/label[1]/img[1]"

    selected_appreciation = random.choice([family, friends, school, me, teacher, technology, math, music, art])

     # Select and click the randomly chosen checkbox
    selected_appreciation_random = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, selected_appreciation))
        )
    selected_appreciation_random.click()
    time.sleep(2)

def submit(driver):

    submit_button = "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/div[1]/button[1]"
    driver.find_element(By.XPATH, submit_button).click()
    time.sleep(2)

def scrollPage(driver):
    main_content_element = driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[3]/form/div/button")

    # Scroll the element into view if it's not visible
    driver.execute_script("arguments[0].scrollIntoView(true);", main_content_element)
    time.sleep(2)

    # Now, scroll the element using its scrollTop property (for vertical scrolling)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", main_content_element)
    time.sleep(2)

    # Alternatively, scroll the element by a certain number of pixels
    driver.execute_script("arguments[0].scrollTop += 500", main_content_element)  # Scroll down 500px
    time.sleep(2)

    # Check if the element is scrollable
    scroll_top = driver.execute_script("return arguments[0].scrollTop;", main_content_element)
    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", main_content_element)
    print(f"Scroll Top: {scroll_top}, Scroll Height: {scroll_height}")


