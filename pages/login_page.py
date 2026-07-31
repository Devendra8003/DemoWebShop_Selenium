from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    LOGIN_LINK = (
        By.CLASS_NAME,
        "ico-login"
    )

    EMAIL = (
        By.ID,
        "Email"
    )

    PASSWORD = (
        By.ID,
        "Password"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "input.login-button"
    )

    LOGOUT_LINK = (
        By.CLASS_NAME,
        "ico-logout"
    )


    def __init__(self, driver):

        super().__init__(driver)



    def open_login(self):

        print("Opening login page")

        self.click(
            self.LOGIN_LINK
        )

        time.sleep(2)



    def enter_email(self,email):

        self.send_keys(
            self.EMAIL,
            email
        )

        print(
            "Email entered:",
            email
        )



    def enter_password(self,password):

        self.send_keys(
            self.PASSWORD,
            password
        )

        print(
            "Password entered"
        )



    def click_login(self):

        self.click(
            self.LOGIN_BUTTON
        )

        print(
            "Login button clicked"
        )



    def login(self,email,password):

        self.open_login()

        self.enter_email(email)

        self.enter_password(password)

        self.click_login()

        time.sleep(3)



    def is_login_successful(self):

        try:

            self.driver.find_element(
                *self.LOGOUT_LINK
            )

            return True

        except:

            return False