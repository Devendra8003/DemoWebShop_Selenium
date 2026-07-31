from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search_page import SearchPage
from pages.product_page import ProductPage

import time


def test_remove_compare(driver):

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
    # ADD TO COMPARE
    # ==========================

    product = ProductPage(driver)

    product.click_compare_product()

    print("Compare button clicked")

    time.sleep(2)

    print("Current URL:", driver.current_url)

    # If not already on compare page, open it
    if "compareproducts" not in driver.current_url:
        product.open_compare_page()
        print("Compare page opened")

    # ==========================
    # CLEAR COMPARE LIST
    # ==========================

    product.clear_compare_list()

    print("Compare list cleared")

    # ==========================
    # VERIFY
    # ==========================

    message = product.get_clear_message()

    print("Message:")
    print(message)

    assert "no items to compare" in message.lower()

    print("Compare product removed successfully.")