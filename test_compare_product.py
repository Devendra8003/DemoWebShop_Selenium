from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.compare_page import ComparePage


def test_compare_product(driver):

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

    # Wait for Compare page
    WebDriverWait(driver, 10).until(
        EC.url_contains("compareproducts")
    )

    print("Compare page opened")

    # ==========================
    # VERIFY
    # ==========================

    compare = ComparePage(driver)

    product_name = compare.get_product_name()

    print("Compared Product:", product_name)

    assert product_name == "Health Book"

    print("Product successfully added to compare list.")