from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ProductPage(BasePage):

    # ==========================
    # LOCATORS
    # ==========================

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "div.product-name h1"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "span.price"
    )

    QUANTITY = (
        By.CSS_SELECTOR,
        "input.qty-input"
    )

    ADD_TO_CART = (
        By.CSS_SELECTOR,
        "input.add-to-cart-button"
    )

    ADD_TO_WISHLIST = (
        By.ID,
        "add-to-wishlist-button-22"
    )

    EMAIL_FRIEND = (
        By.CSS_SELECTOR,
        "input[value='Email a friend']"
    )

    COMPARE_PRODUCT = (
        By.CSS_SELECTOR,
        "input.add-to-compare-list-button"
    )

    COMPARE_LINK = (
        By.LINK_TEXT,
        "Compare products"
    )

    CLEAR_LIST = (
        By.CSS_SELECTOR,
        "a.clear-list"
    )

    NO_DATA = (
        By.CSS_SELECTOR,
        "div.page-body"
    )

    # UPDATED LOCATOR
    ADD_REVIEW = (
        By.LINK_TEXT,
        "Add your review"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "div.bar-notification.success p"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # ==========================
    # PRODUCT DETAILS
    # ==========================

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    # ==========================
    # QUANTITY
    # ==========================

    def enter_quantity(self, quantity):
        self.enter_text(self.QUANTITY, str(quantity))

    # ==========================
    # ADD TO CART
    # ==========================

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    # ==========================
    # WISHLIST
    # ==========================

    def click_add_to_wishlist(self):
        self.click(self.ADD_TO_WISHLIST)

    # ==========================
    # EMAIL FRIEND
    # ==========================

    def click_email_friend(self):
        self.click(self.EMAIL_FRIEND)

    # ==========================
    # COMPARE PRODUCT
    # ==========================

    def click_compare_product(self):

        button = self.wait.until(
            lambda d: d.find_element(*self.COMPARE_PRODUCT)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print("Compare button clicked")

    def get_compare_success_message(self):

        time.sleep(2)

        messages = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.bar-notification.success p"
        )

        if messages:
            return messages[0].text

        return ""

    # ==========================
    # COMPARE PAGE
    # ==========================

    def open_compare_page(self):
        self.driver.get(
            "https://demowebshop.tricentis.com/compareproducts"
        )

    def clear_compare_list(self):
        self.click(self.CLEAR_LIST)

    def get_clear_message(self):
        return self.get_text(self.NO_DATA)

    # ==========================
    # PRODUCT REVIEW
    # ==========================

    def click_add_review(self):

        review_link = self.wait.until(
            lambda d: d.find_element(*self.ADD_REVIEW)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            review_link
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            review_link
        )

        self.wait.until(
            lambda d: "productreviews" in d.current_url
        )

        print("Review page opened")