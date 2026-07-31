from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage

from utils.config import BASE_URL



def test_giftcard(driver):


    # ==========================
    # OPEN WEBSITE
    # ==========================

    driver.get(BASE_URL)



    # ==========================
    # LOGIN
    # ==========================

    login = LoginPage(driver)

    login.login(
        "devendra123@gmail.com",
        "Test@123"
    )



    # ==========================
    # SEARCH PRODUCT
    # ==========================

    search = SearchPage(driver)

    search.search_product(
        "Computing and Internet"
    )



    search.open_product(
        "Computing and Internet"
    )



    # ==========================
    # ADD CART
    # ==========================

    product = ProductPage(driver)

    product.click_add_to_cart()



    # ==========================
    # OPEN CART
    # ==========================

    cart = CartPage(driver)

    cart.open_cart()



    print(
        "Gift card section opened"
    )


    assert cart.is_gift_card_section_displayed()