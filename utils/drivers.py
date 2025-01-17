from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def setup_driver():
    """
    Sets up and returns a WebDriver instance with predefined options.
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--use-gl=swiftshader')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument("--disable-setuid-sandbox")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    return driver
