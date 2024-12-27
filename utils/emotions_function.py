# communicate_helper.py
import random
from selenium.webdriver.common.by import By
import time

def perform_actions(driver):
    # Define the XPaths for the emotions and audio for each section
    communicate = {
        "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
        "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
        "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
        "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/ngx-slider/span[5]",
    }
    communicate_audio = '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/button[1]'

    # Perform action for 'communicate'
    random_communicate = random.choice(list(communicate.values()))
    communicate_element = driver.find_element(By.XPATH, random_communicate)
    communicate_element.click()
    communicate_audio_element = driver.find_element(By.XPATH, communicate_audio)
    communicate_audio_element.click()
    time.sleep(2)

    # Define the XPaths for 'works_together'
    works_together = {
        "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
        "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
        "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
        "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/div/ngx-slider/span[5]",
    }
    works_together_audio = '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/button[1]'

    # Perform action for 'works_together'
    random_works_together = random.choice(list(works_together.values()))
    works_together_element = driver.find_element(By.XPATH, random_works_together)
    works_together_element.click()
    works_together_audio_element = driver.find_element(By.XPATH, works_together_audio)
    works_together_audio_element.click()
    time.sleep(2)

    # Define the XPaths for 'ask_for_help'
    ask_for_help = {
        "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
        "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
        "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
        "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div/ngx-slider/span[5]",
    }
    ask_for_help_audio = '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[3]/button[1]'

    # Perform action for 'ask_for_help'
    random_ask_for_help = random.choice(list(ask_for_help.values()))
    ask_for_help_element = driver.find_element(By.XPATH, random_ask_for_help)
    ask_for_help_element.click()
    ask_for_help_audio_element = driver.find_element(By.XPATH, ask_for_help_audio)
    ask_for_help_audio_element.click()
    time.sleep(2)

    # Define the XPaths for 'ignore_peer_pressure'
    ignore_peer_pressure = {
        "1": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
        "2": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
        "3": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
        "4": "/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[4]/div/ngx-slider/span[5]",
    }
    ignore_peer_pressure_audio = '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[4]/button[1]'

    # Perform action for 'ignore_peer_pressure'
    random_ignore_peer_pressure = random.choice(list(ignore_peer_pressure.values()))
    ignore_peer_pressure_element = driver.find_element(By.XPATH, random_ignore_peer_pressure)
    ignore_peer_pressure_element.click()
    ignore_peer_pressure_audio_element = driver.find_element(By.XPATH, ignore_peer_pressure_audio)
    ignore_peer_pressure_audio_element.click()

    time.sleep(2)
