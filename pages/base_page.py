import time

from selenium.webdriver import ActionChains
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX

"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = 40

    def click_element(self, by_locator):
        element = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", element)


    def input_element(self, by_locator, text):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def verify_title(self, by_locator):
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(by_locator))

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except:
            return False