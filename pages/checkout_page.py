from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    CHECKOUT_TITLE = (
        By.CSS_SELECTOR,
        "div.page-title h1"
    )

    BILLING_CONTINUE = (
        By.XPATH,
        "//input[@onclick='Billing.save()']"
    )

    SHIPPING_ADDRESS_CONTINUE = (
        By.XPATH,
        "//input[@onclick='Shipping.save()']"
    )

    SHIPPING_METHOD_CONTINUE = (
        By.XPATH,
        "//input[@onclick='ShippingMethod.save()']"
    )

    PAYMENT_METHOD_CONTINUE = (
        By.XPATH,
        "//input[@onclick='PaymentMethod.save()']"
    )

    PAYMENT_INFO_CONTINUE = (
        By.XPATH,
        "//input[@onclick='PaymentInfo.save()']"
    )

    CONFIRM_ORDER = (
        By.XPATH,
        "//input[@onclick='ConfirmOrder.save()']"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "div.title strong"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    # -----------------------------

    def js_click(self, locator):

        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # -----------------------------

    def accept_terms(self):

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                self.TERMS_CHECKBOX
            )
        )

        if not checkbox.is_selected():
            checkbox.click()

    # -----------------------------

    def click_checkout(self):

        self.js_click(self.CHECKOUT_BUTTON)

    # -----------------------------

    def get_checkout_title(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.CHECKOUT_TITLE
            )
        ).text

    # -----------------------------

    def billing_continue(self):

        self.js_click(self.BILLING_CONTINUE)

    # -----------------------------

    def shipping_address_continue(self):

        self.js_click(self.SHIPPING_ADDRESS_CONTINUE)

    # -----------------------------

    def shipping_method_continue(self):

        self.js_click(self.SHIPPING_METHOD_CONTINUE)

    # -----------------------------

    def payment_method_continue(self):

        self.js_click(self.PAYMENT_METHOD_CONTINUE)

    # -----------------------------

    def payment_information_continue(self):

        self.js_click(self.PAYMENT_INFO_CONTINUE)

    # -----------------------------

    def confirm_order(self):

        self.js_click(self.CONFIRM_ORDER)

    # -----------------------------

    def verify_order_success(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        ).text