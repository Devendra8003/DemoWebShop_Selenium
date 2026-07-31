from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver
from utils.config import BASE_URL, EMAIL, PASSWORD
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage


def test_product_details():

    driver = get_driver()

    try:
        # Open Website
        driver.get(BASE_URL)

        # ---------------- LOGIN ----------------
        login = LoginPage(driver)
        login.login(EMAIL, PASSWORD)

        # Verify login successful
        assert login.is_login_successful()

        # ---------------- SEARCH PRODUCT ----------------
        search = SearchPage(driver)
        search.search_product("Computing and Internet")

        # Click product from search result
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Computing and Internet")
            )
        ).click()

        # ---------------- PRODUCT DETAILS ----------------
        product = ProductPage(driver)

        product_name = product.get_product_name()
        product_price = product.get_product_price()

        print("Product Name:", product_name)
        print("Product Price:", product_price)

        # Verify product details
        assert product_name == "Computing and Internet"
        assert product_price == "800.00"

        # ---------------- ADD TO CART ----------------
        product.enter_quantity(2)
        product.click_add_to_cart()

        success_message = product.get_success_message()

        print(success_message)

        # Verify cart message
        assert "added to your shopping cart" in success_message

    finally:
        driver.quit()