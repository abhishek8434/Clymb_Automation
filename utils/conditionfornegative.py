from selenium.webdriver.common.by import By
import time
def reload_check_self_awareness(driver):
    # Locate the heading element (e.g., <h1>) and get its text
    # Locate the heading element using XPath
    heading_element = driver.find_element(By.XPATH, '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h2[1]')

    # Fetch the text of the heading element
    heading_text_self_awareness = heading_element.text

    # Verify the heading
    expected_heading = "Self-Awareness"
    if heading_text_self_awareness == expected_heading:
        print("Heading is correct.")
    else:
        print(f"Heading is incorrect. Found: {heading_text_self_awareness}")
    time.sleep(1)
    return heading_text_self_awareness


def reload_check_responsible_decision_making(driver):
    # Locate the heading element (e.g., <h1>) and get its text
    # Locate the heading element using XPath
    heading_element = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/h2')

    # Fetch the text of the heading element
    heading_text_responsible_decision_making = heading_element.text

    # Verify the heading
    expected_heading = "Responsible Decision-Making Skill"
    if heading_text_responsible_decision_making == expected_heading:
        print("Heading is correct.")
    else:
        print(f"Heading is incorrect. Found: {heading_text_responsible_decision_making}")
    time.sleep(1)    
    return heading_text_responsible_decision_making

def reload_check_self_management(driver):
    # Locate the heading element (e.g., <h1>) and get its text
    # Locate the heading element using XPath
    heading_element = driver.find_element(By.XPATH, '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h2[1]')

    # Fetch the text of the heading element
    heading_text_self_management = heading_element.text

    # Verify the heading
    expected_heading = "Self-Management"
    if heading_text_self_management == expected_heading:
        print("Heading is correct.")
    else:
        print(f"Heading is incorrect. Found: {heading_text_self_management}")
    time.sleep(1)
    return heading_text_self_management

def reload_check_social_awareness(driver):
    # Locate the heading element (e.g., <h1>) and get its text
    # Locate the heading element using XPath
    heading_element = driver.find_element(By.XPATH, '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h2[1]')

    # Fetch the text of the heading element
    heading_text_social_awareness = heading_element.text

    # Verify the heading
    expected_heading = "Social Awareness"
    if heading_text_social_awareness == expected_heading:
        print("Heading is correct.")
    else:
        print(f"Heading is incorrect. Found: {heading_text_social_awareness}")
    time.sleep(1)
    return heading_text_social_awareness

def reload_check_relationship_skills(driver):
    # Locate the heading element (e.g., <h1>) and get its text
    # Locate the heading element using XPath
    heading_element = driver.find_element(By.XPATH, '/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h2[1]')

    # Fetch the text of the heading element
    heading_text_relationship_skill = heading_element.text

    # Verify the heading
    expected_heading = "Relationship Skills"
    if heading_text_relationship_skill == expected_heading:
        print("Heading is correct.")
    else:
        print(f"Heading is incorrect. Found: {heading_text_relationship_skill}")
    time.sleep(1)
    return heading_text_relationship_skill


