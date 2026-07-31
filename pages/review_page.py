from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReviewPage:

    REVIEW_TITLE = (By.ID, "AddProductReview_Title")
    REVIEW_TEXT = (By.ID, "AddProductReview_ReviewText")
    RATING = (By.ID, "addproductrating_5")
    SUBMIT_BUTTON = (
        By.NAME,
        "add-review"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".result"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        ".validation-summary-errors"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -----------------------------
    # Review Title
    # -----------------------------
    def enter_review_title(self, title):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.REVIEW_TITLE
            )
        )

        element.click()
        element.clear()
        element.send_keys(title)

        print("Review title entered")

    # -----------------------------
    # Review Text
    # -----------------------------
    def enter_review_text(self, text):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.REVIEW_TEXT
            )
        )

        element.click()
        element.clear()
        element.send_keys(text)

        print("Review text entered")

    # -----------------------------
    # Rating
    # -----------------------------
    def select_rating(self):

        rating = self.wait.until(
            EC.element_to_be_clickable(
                self.RATING
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            rating
        )

        print("Rating selected")

    # -----------------------------
    # Submit
    # -----------------------------
    def click_submit_review(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print("Submit button clicked")

    # -----------------------------
    # Success Message
    # -----------------------------
    def get_success_message(self):

        try:

            msg = self.wait.until(
                EC.visibility_of_element_located(
                    self.SUCCESS_MESSAGE
                )
            )

            return msg.text

        except Exception:

            return ""

    # -----------------------------
    # Error Message
    # -----------------------------
    def get_error_message(self):

        try:

            msg = self.wait.until(
                EC.visibility_of_element_located(
                    self.ERROR_MESSAGE
                )
            )

            return msg.text

        except Exception:

            return ""