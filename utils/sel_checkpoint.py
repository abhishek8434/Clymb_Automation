import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import logging

def select_sel(driver):
    sel_button_xpath = "//li[@class='li-hidden']//a[@class='btn btn-danger'][normalize-space()='Start SEL Checkpoint']"
    sel_button_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, sel_button_xpath))
    )
    sel_button_element.click()
    time.sleep(2)

def first_question(driver):
    options_for_first_question = {
        "option1": "//label[normalize-space()='Not like me at all']",
        "option2": "//label[normalize-space()='Not much like me']",
        "option3": "//label[normalize-space()='Somewhat like me']",
        "option4": "//label[normalize-space()='Very much like me']",
    }

    # Select a random emotion
    random_options_for_first_question = random.choice(list(options_for_first_question.values()))

    # Locate and click on the randomly selected emotion
    options_for_first_question_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, random_options_for_first_question)))
    options_for_first_question_element.click()
    time.sleep(2)
    
def next_button(driver):
    next_button_xpath = "/html/body/ngb-modal-window/div/div/app-socio-competancy/div/div/div/div[1]/div/div[2]/div[2]/button"
    next_button_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, next_button_xpath))
    )
    next_button_element.click()
    time.sleep(2)
       
def submit_button(driver):
    submit_button_xpath = "/html/body/ngb-modal-window/div/div/app-socio-competancy/div/div/div/div[1]/div/div[2]/div[2]/button"
    submit_button_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, submit_button_xpath))
    )
    submit_button_element.click()
    
    
def verify_message_after_submit(driver):
   
    time.sleep(2)
    success_message_xpath = "(//h2[normalize-space()='SEL Checkpoint submitted successfully.'])[1]"
    
    success_message_fetch = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, success_message_xpath))
    )
    
    # Get the text of the success message
    success_message_text = success_message_fetch.text
    
    # Expected success message value
    success_message_value = "SEL Checkpoint submitted successfully."
    
    # Compare the text and print the result
    if success_message_text == success_message_value:
        logging.info("SEL Checkpoint submitted successfully.")
    else:
        logging.info(f"Extracted message: '{success_message_text}'")