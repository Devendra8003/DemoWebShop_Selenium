from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmailFriendPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )


    # ==========================
    # LOCATORS
    # ==========================

    FRIEND_EMAIL = (
        By.ID,
        "FriendEmail"
    )


    YOUR_EMAIL = (
        By.ID,
        "YourEmailAddress"
    )


    MESSAGE = (
        By.ID,
        "PersonalMessage"
    )


    SEND_BUTTON = (
        By.CSS_SELECTOR,
        "input.send-email-a-friend-button"
    )


    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".result"
    )


    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        ".validation-summary-errors li"
    )



    # ==========================
    # ENTER FRIEND EMAIL
    # ==========================

    def enter_friend_email(self, email):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.FRIEND_EMAIL
            )
        )

        field.clear()

        field.send_keys(email)

        print("Friend email entered")



    # ==========================
    # ENTER YOUR EMAIL
    # ==========================

    def enter_your_email(self, email):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.YOUR_EMAIL
            )
        )

        field.clear()

        field.send_keys(email)

        print("Your email entered")



    # ==========================
    # ENTER MESSAGE
    # ==========================

    def enter_message(self, message):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.MESSAGE
            )
        )

        field.clear()

        field.send_keys(message)

        print("Message entered")



    # ==========================
    # CLICK SEND EMAIL
    # ==========================

    def click_send(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.SEND_BUTTON
            )
        )


        # JavaScript click (more stable)
        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


        print("Send email clicked")



    # ==========================
    # GET ERROR MESSAGE
    # ==========================

    def get_error_message(self):

        try:

            error = self.wait.until(
                EC.visibility_of_element_located(
                    self.ERROR_MESSAGE
                )
            )

            return error.text


        except Exception:

            try:

                error = self.driver.find_element(
                    By.CLASS_NAME,
                    "message-error"
                )

                return error.text


            except Exception:

                return ""



    # ==========================
    # GET SUCCESS MESSAGE
    # ==========================

    def get_success_message(self):

        try:

            success = self.wait.until(
                EC.visibility_of_element_located(
                    self.SUCCESS_MESSAGE
                )
            )

            return success.text


        except Exception:

            return ""