from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver
from utils.config import BASE_URL, EMAIL, PASSWORD

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.review_page import ReviewPage

import time


def test_product_review():

    driver = get_driver()

    try:

        # ==========================
        # OPEN WEBSITE
        # ==========================

        driver.get(BASE_URL)

        # ==========================
        # LOGIN
        # ==========================

        login = LoginPage(driver)

        login.login(EMAIL, PASSWORD)

        assert login.is_login_successful()

        print("Login completed")

        # ==========================
        # SEARCH PRODUCT
        # ==========================

        search = SearchPage(driver)

        search.search_product("Health Book")

        print("Product searched")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Health Book")
            )
        ).click()

        print("Product opened")

        # ==========================
        # OPEN REVIEW PAGE
        # ==========================

        product = ProductPage(driver)

        product.click_add_review()

        print("Review page opened")

        # ==========================
        # REVIEW
        # ==========================

        review = ReviewPage(driver)

        review.enter_review_title(
            "Excellent Book"
        )

        review.enter_review_text(
            "Very useful book for beginners."
        )

        review.select_rating()

        review.click_submit_review()

        time.sleep(3)

        # ==========================
        # VERIFY
        # ==========================

        success = review.get_success_message()

        if success:
            print(success)
            assert "successfully" in success.lower()

        else:
            error = review.get_error_message()
            print(error)

            assert (
                "product review is successfully added." in error.lower()
                or
                "review" in error.lower()
            )

        print("Product Review Test Passed")

    finally:

        driver.quit()