from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def before_scenario(context, scenario):
    dirname = os.path.dirname(__file__)

    # Specify the path to the ChromeDriver executable
    driver_path = os.path.join(dirname, "drivers", "chromedriver.exe")

    # Create a Service object with the path to the ChromeDriver executable
    chrome_service = Service(driver_path)

    # Create a new instance of Options
    chrome_options = Options()

    # Initialize the WebDriver with the correct service and options
    context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    context.driver.maximize_window()
    print("Chrome browser launched successfully")


def after_scenario(context, scenario):
    context.driver.quit()
