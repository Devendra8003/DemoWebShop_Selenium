from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver
from utils.config import BASE_URL, EMAIL, PASSWORD

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage


def test_wishlist():

    driver = get_driver()

    try:
        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login(EMAIL, PASSWORD)

        assert login.is_login_successful()

        search = SearchPage(driver)
        search.search_product("Health Book")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                ((By.LINK_TEXT, "Health Book"))
            )
        ).click()
        print("Current URL:", driver.current_url)
        print("Page Title:", driver.title)

        driver.save_screenshot("product_page.png")

        import time

        time.sleep(3)

        print("Current URL:", driver.current_url)
        print("Page Title:", driver.title)

        product = ProductPage(driver)

        product.enter_quantity(1)

        product.click_add_to_wishlist()

        print(product.get_success_message())

        wishlist = WishlistPage(driver)

        wishlist.open_wishlist()

        print("Product:", wishlist.get_product_name())
        print("Quantity:", wishlist.get_quantity())

        assert wishlist.get_product_name() == "Health Book"

        wishlist.remove_product()

        print(wishlist.get_empty_message())

    finally:
        driver.quit()