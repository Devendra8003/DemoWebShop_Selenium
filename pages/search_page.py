from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.button-1.search-box-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def search_product(self, product):

        print(f"Searching product: {product}")

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        search.clear()
        search.send_keys(product)


        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()


        print("Search completed")



    def open_product(self, product_name):

        product = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, product_name)
            )
        )

        product.click()

        print("Product opened")