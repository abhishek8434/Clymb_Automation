import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def verify_names(driver):
    user_name_xpath = "//app-header/header/div/h1"
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, user_name_xpath))
        )
        element_found = element.text.strip()
        print(f"Fetched text: {element_found}")

        # Extract name
        if ", " in element_found:
            name = element_found.split(", ")[-1].split()[0].strip('?')
            print(f"Extracted name: {name}")
            return name
        else:
            print("Name not found.")
            return None
    except Exception as e:
        print(f"An error occurred in verify_names: {e}")
        return None



def verify_name_admin_notification(driver, extracted_name):
    try:
        # Fetch admin notification text
        user_name_on_admin_xpath = "//mat-dialog-container//ul/li/div/label"
        user_name_on_admin_fetch = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, user_name_on_admin_xpath))
        )
        user_name_on_admin = user_name_on_admin_fetch.text.strip()

        print(f"Admin notification name: {user_name_on_admin}")

        # Check if the extracted name is in the admin notification name
        if extracted_name and extracted_name in user_name_on_admin:
            print("Extracted name is found in the admin notification.")
            time.sleep(2)
            # Click on 'View' button
            click_on_view_xpath = "//mat-dialog-container//button/span[contains(text(),'View')]"
            click_on_view_fetch = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, click_on_view_xpath))
            )
            click_on_view_fetch.click()
            
            time.sleep(5)
            
            notitification_name_fetch_xpath = "//body[1]/fuse-root[1]/div[1]/main[1]/app-afh-notify[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]"
            notification_name_fetch = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, notitification_name_fetch_xpath))
            )
            
            notification_name = notification_name_fetch.text.strip()
            print(f"Admin notification Tab: {notification_name}")
            if extracted_name and extracted_name in user_name_on_admin:
                print("Extracted name is found in the admin notification Tab.")
            else:
                print(f"Extracted name '{extracted_name}' not found in admin name: '{notification_name}'")

        else:
            print(f"Extracted name '{extracted_name}' not found in admin name: '{user_name_on_admin}'")
    except Exception as e:
        print(f"An error occurred in verify_name_admin_notification: {e}")


    
   
    
