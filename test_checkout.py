from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout(driver):

    # ==========================
    # LOGIN
    # ==========================

    login = LoginPage(driver)

    login.login(
        "devendra123@gmail.com",
        "Test@123"
    )

    print("Login completed")

    assert login.is_login_successful()

    # ==========================
    # CLEAR CART
    # ==========================

    cart = CartPage(driver)

    cart.clear_cart()

    # ==========================
    # SEARCH PRODUCT
    # ==========================

    search = SearchPage(driver)

    search.search_product("Health Book")

    search.open_product("Health Book")

    print("Product searched and opened")

    # ==========================
    # ADD TO CART
    # ==========================

    product = ProductPage(driver)

    product.enter_quantity(1)

    product.click_add_to_cart()

    print(product.get_success_message())

    # ==========================
    # OPEN CART
    # ==========================

    cart.open_cart()

    print("Cart opened")

    print("Product:", cart.get_product_name())

    print("Quantity:", cart.get_quantity())

    # ==========================
    # CHECKOUT
    # ==========================

    checkout = CheckoutPage(driver)

    checkout.accept_terms()

    print("Terms accepted")

    checkout.click_checkout()

    print("Checkout button clicked")

    print("Page:", checkout.get_checkout_title())

    # ==========================
    # BILLING ADDRESS
    # ==========================

    checkout.billing_continue()

    print("Billing Address Completed")

    # ==========================
    # SHIPPING ADDRESS
    # ==========================

    checkout.shipping_address_continue()

    print("Shipping Address Completed")

    # ==========================
    # SHIPPING METHOD
    # ==========================

    checkout.shipping_method_continue()

    print("Shipping Method Completed")

    # ==========================
    # PAYMENT METHOD
    # ==========================

    checkout.payment_method_continue()

    print("Payment Method Completed")

    # ==========================
    # PAYMENT INFORMATION
    # ==========================

    checkout.payment_information_continue()

    print("Payment Information Completed")

    # ==========================
    # CONFIRM ORDER
    # ==========================

    checkout.confirm_order()

    print("Order Confirmed")

    # ==========================
    # VERIFY SUCCESS
    # ==========================

    result = checkout.verify_order_success()

    print("Result:", result)

    assert "successfully processed" in result.lower()

    print("Checkout Test Passed")