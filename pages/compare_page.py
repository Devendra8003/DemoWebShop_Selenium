from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComparePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "tr.product-name td a"
    )

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text


    