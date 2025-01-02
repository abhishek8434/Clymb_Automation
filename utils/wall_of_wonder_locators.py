import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import random


def wall_of_wonder_create(driver):
   
    
    wall_of_wonder_xpath = "//a[@routerlink='/dashboard/post']"
    
    select_wall_of_wonder = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, wall_of_wonder_xpath))
    )
    click_on_wall_of_wonder = select_wall_of_wonder.click()
    
    
    click_on_wall_xpath = "//textarea[@id='textarea-editor']"
    select_click_on_wall = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, click_on_wall_xpath))
    )   
    enter_text_on_wall = select_click_on_wall.send_keys("Hello Had a Great Morning Ahead!")
    
    
def click_on_submit_wall(driver):
    
    click_on_wall_submit_xpath = "//textarea[@id='textarea-editor']"
    

    select_click_on_wall_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, click_on_wall_submit_xpath))
    )
    
    click_on_wall_submit = select_click_on_wall_submit.click()
    
def click_on_add_photo(driver):
    
    click_on_add_xpath = "//button[normalize-space()='Add Photo']"
    

    select_click_on_add_image = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, click_on_add_xpath))
    )
    
    click_on_wall_submit = select_click_on_add_image.click()
    
       
def random_photo_select(driver):  
    
    # Find the scrollable container inside the popup
    popup = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-select-wow-images/div/div/div")

    # Get the initial scroll height of the popup
    last_height = driver.execute_script("return arguments[0].scrollHeight", popup)

    while True:
        # Scroll down a little inside the popup
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)

        # Wait for new content to load (adjust time as needed based on load speed)
        time.sleep(3)

        # Get the new scroll height of the popup after scrolling
        new_height = driver.execute_script("return arguments[0].scrollHeight", popup)

        # If the new scroll height is the same as the last height, we've reached the end of the popup
        if new_height == last_height:
            break
        
        last_height = new_height

    # Wait until the labels are visible inside the popup
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/ngb-modal-window/div/div/app-select-wow-images/div/div/div/div/div/div/div/label")))

    # Now, count the labels after scrolling to the bottom of the popup
    labels = driver.find_elements(By.XPATH, "/html/body/ngb-modal-window/div/div/app-select-wow-images/div/div/div/div/div/div/div/label")
    
    # Count the labels
    label_count = len(labels)

    # Print the count
    print(f"Count of labels: {label_count}")
    
    if label_count > 0:
        # Randomly select 5 labels (or fewer if there are less than 5)
        random_labels = random.sample(labels, min(5, label_count))

          # Output the randomly selected labels, their IDs, and click them
        for i, label in enumerate(random_labels, start=0):  # Start from 0 for label indices
            # Assuming you have already located the label element
            label_for = label.get_attribute("for")
            print(f"Selected Label {i} with ID:{label_for}")
            label.click()  # Click the randomly selected label
            time.sleep(1)  # Adding a small delay between clicks (adjust as needed)
            
    
    
 
    save_image_xpath = "//button[normalize-space()='Save']"
    

    select_save_image_image = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, save_image_xpath))
    )
    
    click_on_save_button = select_save_image_image.click()
    

    
def make_post(driver):
    make_post_xpath = "//button[normalize-space()='Post']"
    

    select_make_post_image = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, make_post_xpath))
    )
    
    click_on_post_button = select_make_post_image.click()
    