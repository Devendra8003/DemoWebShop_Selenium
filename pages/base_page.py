from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )


    # ===============================
    # CLICK ELEMENT
    # ===============================

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()



    # ===============================
    # ENTER TEXT
    # ===============================

    def enter_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)



    # ===============================
    # SEND KEYS ALIAS
    # ===============================

    def send_keys(self, locator, text):

        self.enter_text(
            locator,
            text
        )



    # ===============================
    # GET TEXT
    # ===============================

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text



    # ===============================
    # FIND ELEMENT
    # ===============================

    def find_element(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )



    # ===============================
    # CHECK DISPLAYED
    # ===============================

    def is_displayed(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()


        except TimeoutException:

            return False