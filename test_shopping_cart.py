from utils.driver_factory import get_driver
from utils.config import BASE_URL, EMAIL, PASSWORD
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart():

    driver = get_driver()

    try:
        # Open Website
        driver.get(BASE_URL)

        # Login
        login = LoginPage(driver)
        login.login(EMAIL, PASSWORD)

        # Verify Login
        assert login.is_login_successful()

        cart = CartPage(driver)
        cart.clear_cart()

        # Search Product
        search = SearchPage(driver)
        search.search_product("Computing and Internet")

        # Open Product
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Computing and Internet")
            )
        ).click()

        # Product Page
        product = ProductPage(driver)

        # Add to Cart
        product.enter_quantity(2)
        product.click_add_to_cart()

        # Verify Success Message
        success_message = product.get_success_message()
        print(success_message)

        assert "added to your shopping cart" in success_message

        # Open Shopping Cart
        cart = CartPage(driver)
        cart.open_cart()

        # Verify Product Name
        product_name = cart.get_product_name()
        print("Product in Cart:", product_name)

        assert product_name == "Computing and Internet"

        # Verify Quantity
        quantity = cart.get_quantity()
        print("Quantity:", quantity)

        assert quantity == "2"

        # Remove Product
        cart.remove_product()

        # Verify Empty Cart
        empty_message = cart.get_empty_cart_message()
        print(empty_message)

        assert "Your Shopping Cart is empty!" in empty_message

    finally:
        driver.quit()