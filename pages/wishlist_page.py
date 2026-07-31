from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WishlistPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    WISHLIST_LINK = (By.LINK_TEXT, "Wishlist")
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.product a")
    QUANTITY = (By.CSS_SELECTOR, "input.qty-input")
    REMOVE = (By.NAME, "removefromcart")
    UPDATE = (By.NAME, "updatecart")
    EMPTY = (By.CSS_SELECTOR, "div.wishlist-content")

    def open_wishlist(self):
        self.wait.until(
            EC.element_to_be_clickable(self.WISHLIST_LINK)
        ).click()

        # Save the Wishlist page HTML
        with open("wishlist_page.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)

        print("Wishlist HTML saved")

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    def get_quantity(self):
        return self.driver.find_element(
            *self.QUANTITY
        ).get_attribute("value")

    def remove_product(self):
        self.driver.find_element(*self.REMOVE).click()
        self.driver.find_element(*self.UPDATE).click()

    def get_empty_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.EMPTY)
        ).text