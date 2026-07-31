from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_remove_cart(driver):

    # ==========================
    # SEARCH PRODUCT
    # ==========================

    search = SearchPage(driver)

    search.search_product("Computing and Internet")

    print("Product searched")


    # ==========================
    # OPEN PRODUCT
    # ==========================

    search.open_product("Computing and Internet")

    print("Product opened")


    # ==========================
    # ADD PRODUCT TO CART
    # ==========================

    product = ProductPage(driver)

    product.click_add_to_cart()

    print("Product added to cart")


    # ==========================
    # OPEN CART
    # ==========================

    cart = CartPage(driver)

    cart.open_cart()

    print("Cart opened")


    # ==========================
    # REMOVE PRODUCT
    # ==========================

    cart.remove_product()

    print("Product removed from cart")


    # ==========================
    # VERIFY CART EMPTY
    # ==========================

    message = cart.get_empty_cart_message()

    print("Cart Message:", message)


    assert "Your Shopping Cart is empty" in message


    print("Remove cart test passed")