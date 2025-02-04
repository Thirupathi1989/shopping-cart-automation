from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import  WebDriverWait
import random

class ShoppingCartPage(BasePage):

    page_title = (By.XPATH, "//title[contains(text(),'Shopping cart')]")
    ipt_size_selection = "//input[@data-testid='checkbox' and @value=\'<size>\']//parent::label"
    free_shipping = "//*[text()='Free shipping']//parent::*//button"
    without_free_shipping = "//div[contains(@class,'sc-124al1g-2')]"
    fetch_product_count = (By.XPATH, "//main[@class='sc-ebmerl-4 iliWeY']//p")
    cart_items_count = (By.XPATH, "//div[contains(@class,'sc-1h98xa9-3')]")
    add_product_from_cart_items = "//*[text()=\'<product>\']//ancestor::div[contains(@class,'sc-11uohgb-0')]//button[text()='+']"
    remove_button = "//div[@class='sc-11uohgb-0 hDmOrM']//button[@title='remove product from cart']"
    check_out = (By.XPATH, "//button[text()='Checkout']")
    fetch_product_price = (By.XPATH, "(//div[@class='sc-1h98xa9-8 bciIxg']//p)[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.size_selection = None
        self.add_product_from_cart =None

    def validate_page_title(self):
        self.verify_title(self.page_title)

    def add_item_to_cart(self):
        self.click_element(self.ipt_size_selection)

    def select_different_size(self, size):
        self.size_selection = (By.XPATH,self.ipt_size_selection.replace('<size>',size))
        self.click_element(self.size_selection)
        time.sleep(10)

    def fetch_product_details(self):
        product_count = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(self.fetch_product_count)).text
        # Extract integers
        count_value = [int(word) for word in product_count.split() if word.isdigit()]

        return count_value[0]

    def fetch_cart_items_details(self):
        cart_items = self.get_element_text(self.cart_items_count)
        return cart_items

    def select_free_shipping_product(self):
        free_shipping_items = self.driver.find_elements_by_xpath(self.free_shipping)
        #selected_items = random.sample(free_shipping_items, 4)
        for i in range(1, 4):
            for item in free_shipping_items:
                if i <=4:
                    item.click()
            if i > 4:
                break

    def select_without_free_shipping_product(self):
        shipping_items = self.driver.find_elements_by_xpath(self.without_free_shipping)
        for i in len(shipping_items):
            elements = self.driver.find_elements_by_xpath("(//div[contains(@class,'sc-124al1g-2')])"+"["+i+"]"+"//div[@class='sc-124al1g-3 bHJSNa']")
            if len(elements)==0:
                self.driver.find_element_by_xpath("(//button[text()='Add to cart'])["+i+"]").click()
                break

    def add_product_using_card_items(self, product):
        self.add_product_from_cart = (By.XPATH,self.add_product_from_cart_items.replace('<product>',product))
        self.click_element(self.add_product_from_cart)
        time.sleep(10)

    def remove_product_using_card_items(self):
        remove_cart = self.driver.find_elements_by_xpath(self.remove_button)
        for item in remove_cart:
            item.click()
            time.sleep(5)

    def click_checkout(self):
        self.click_element(self.check_out)

    def fetch_price_details(self):
        price_count = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(self.fetch_product_price)).text
        # Extract integers
        count_value = [int(word) for word in price_count.split() if word.isdigit()]
        return count_value[0]