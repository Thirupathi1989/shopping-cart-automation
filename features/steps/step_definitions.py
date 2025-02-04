from behave import *
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.shopping_cart_page import ShoppingCartPage
from testdata.conf import Data as data
import logging
from selenium.webdriver.common.alert import Alert


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

@given('launch the browser')
def launchBrowser(context):
    try:
        if data.BROWSER == 'chrome':
            # Get the directory name of the current file
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
    except:
        raise ValueError('Browser is not supported')


@when('open firebase homepage')
def openFirebasePage(context):
    try:
        context.driver.get(data.URL)
        context.cardPage = ShoppingCartPage(context.driver)
    except:
        context.driver.close()
        assert False, "Test is failed in open login page section"


@then('user validate shopping card page title')
def verifyTitle(context):
    try:
        context.cardPage.validate_page_title()
    except:
        context.driver.close()
        assert False, "Test is failed due to invalid page title"


@when('the user selects size "{size}"')
def select_size(context, size):
    try:
        context.cardPage.select_different_size(size)
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to select different sizes"


@when('the user selects different size "{size}"')
def select_different_size(context, size):
    try:
        context.cardPage.select_different_size(size)
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to select different sizes"


@when('the user filtered multiple size "{size1}" and "{size2}"')
def select_multiple_size(context, size1, size2):
    try:
        context.cardPage.select_different_size(size1)
        context.cardPage.select_different_size(size2)
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to select different sizes"

@then('the items displayed should be filtered by size "{size}"')
def validate_available_product_count_based_on_size(context, size):
    try:
        product_count = context.cardPage.fetch_product_details()
        logger.info("total product count is " + str(product_count))
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to fetch product count"

@then('the total count based on filtered by sizes is "{total_count}"')
def validate_product_count(context, total_count):
    try:
        product_count = context.cardPage.fetch_product_details()
        if int(total_count) == int(product_count):
            logger.info("total product count is " + str(product_count))
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to fetch product count"


@then('the total items count is "{total_count}"')
def validate_product_count_based_on_size(context, size, total_count):
    try:
        product_count = context.cardPage.fetch_product_details()
        if int(total_count) == int(product_count):
            logger.info("total product count is " + str(product_count))
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to fetch product count"


@when('the user adds 4 random items with Free shipping to the cart')
def step_when_user_adds_free_shipping_items(context):
    try:
        context.cardPage.select_free_shipping_product()
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to select free shipping"


@when('the user adds 1 random items without Free shipping to the cart')
def step_when_user_adds_free_shipping_items(context):
    try:
        context.cardPage.select_without_free_shipping_product()
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to select without free shipping"


@then('the total cart item count is "{total_count}"')
def validate_cart_item(context, total_count):
    try:
        cart_count = context.cardPage.fetch_cart_items_details()
        if int(total_count) == int(cart_count):
            logger.info("total cart count is " + str(cart_count))
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to fetch product count"


@then('add the "{product}" item using cart')
def select_product_using_cart(context, product):
    try:
        context.cardPage.add_product_using_card_items(product)
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to add product from cart"


@then('remove all the product from cart item')
def remove_product_using_cart(context):
    try:
        context.cardPage.remove_product_using_card_items()
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to remove product from cart"

@then('user click checkout')
def check_out_button(context):
    try:
        context.cardPage.click_checkout()
    except:
        context.driver.close()
        assert False, "Test is failed due to unable to click checkout from cart"


@then('an alert message should be displayed with the correct price as the cart total')
def step_then_verify_alert_message_with_correct_price(context):
    alert = Alert(context.browser)
    total_price = float(context.browser.find_element_by_xpath("(//div[@class='sc-1h98xa9-8 bciIxg']//p)[1]").text.strip('$'))
    assert str(total_price) in alert.text, f"Expected alert message with total price {total_price}, but got {alert.text}"
    alert.accept()

@when('the user refreshes the page')
def step_when_user_refreshes_page(context):
    context.browser.refresh()

@then('the items in the cart should be reset')
def step_then_verify_cart_is_reset(context):
    total_price = float(context.browser.find_element_by_xpath("(//div[@class='sc-1h98xa9-8 bciIxg']//p)[1]").text.strip('$'))
    assert total_price == 0, f"Expected total price 0, but got {total_price}"

@then('close the browser')
def closeBrowser(context):
    context.driver.close()
