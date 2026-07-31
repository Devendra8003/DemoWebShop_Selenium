from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_cart(driver):
    cart = CartPage(driver)
    cart.clear_cart()
    # Search Product
    search = SearchPage(driver)
    search.search_product("Health Book")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Health Book")
        )
    ).click()

    # Product Page
    product = ProductPage(driver)

    product.enter_quantity(2)

    product.click_add_to_cart()

    print(product.get_success_message())

    # Cart Page
    cart = CartPage(driver)

    cart.open_cart()

    print("Product:", cart.get_product_name())
    print("Quantity:", cart.get_quantity())

    assert cart.get_product_name() == "Health Book"

    cart.remove_product()

    print(cart.get_empty_cart_message())

    assert cart.get_empty_cart_message() == "Your Shopping Cart is empty!"