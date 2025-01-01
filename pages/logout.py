from selenium.webdriver.common.by import By
import time

def logout_to_application(driver):
    

    # Step 1: Logout
    try:
        profile_dropdown = '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-header[1]/header[1]/div[1]/ul[1]/li[4]/div[1]/div[1]'
        profile_logout = '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-header[1]/header[1]/div[1]/ul[1]/li[4]/div[1]/div[2]/ul[1]/li[4]/a[1]'
        logout_confirmation = '/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-confirm-dialog[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]'

        profile_dropdown_element = driver.find_element(By.XPATH, profile_dropdown)
        profile_dropdown_element.click()
        time.sleep(1)

        profile_logout_element = driver.find_element(By.XPATH, profile_logout)
        profile_logout_element.click()
        time.sleep(1)

        logout_confirmation_element = driver.find_element(By.XPATH, logout_confirmation)
        logout_confirmation_element.click()
        time.sleep(1)


        # Wait for login process to complete
        time.sleep(5)
    except Exception as e:
        print(f"Error during logout: {e}")
