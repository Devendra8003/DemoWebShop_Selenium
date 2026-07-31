from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage



def test_coupon(driver):

    # ==========================
    # SEARCH PRODUCT
    # ==========================

    search = SearchPage(driver)

    search.search_product("Health Book")

    print("Product searched")


    # ==========================
    # OPEN PRODUCT
    # ==========================

    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT,"Health Book")
        )
    ).click()


    print("Product opened")


    # ==========================
    # ADD TO CART
    # ==========================

    product = ProductPage(driver)

    product.click_add_to_cart()


    print("Added to cart")


    # ==========================
    # OPEN CART
    # ==========================

    cart = CartPage(driver)

    cart.open_cart()


    print("Cart opened")


    # ==========================
    # COUPON TEST
    # ==========================

    result = cart.enter_coupon("TEST123")


    assert result == True


    print("Coupon test completed")