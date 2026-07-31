from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================
    # LOCATORS
    # =========================

    CART_LINK = (
        By.CLASS_NAME,
        "cart-label"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "td.product a"
    )

    QUANTITY = (
        By.CSS_SELECTOR,
        "input.qty-input"
    )

    REMOVE_CHECKBOX = (
        By.NAME,
        "removefromcart"
    )

    UPDATE_CART = (
        By.NAME,
        "updatecart"
    )
    COUPON_BOX = (
        By.NAME,
        "discountcouponcode"
    )

    APPLY_COUPON = (
        By.NAME,
        "applydiscountcouponcode"
    )

    GIFT_CARD_TEXT = (
        By.XPATH,
        "//div[@class='giftcard-box']"
    )

    EMPTY_CART_MESSAGE = (
        By.CSS_SELECTOR,
        "div.order-summary-content"
    )

    # =========================
    # OPEN CART
    # =========================

  def open_cart(self):
    # Wait for the "added to cart" banner to disappear first
    try:
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "div.bar-notification.success")
            )
        )
    except Exception:
        pass

    cart_link = self.wait.until(
        EC.element_to_be_clickable(self.CART_LINK)
    )
    # JS click as a safety net in case something else still overlaps
    self.driver.execute_script("arguments[0].click();", cart_link)

    # =========================
    # PRODUCT NAME
    # =========================

    def get_product_name(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_NAME
            )
        ).text

    # =========================
    # QUANTITY
    # =========================

    def get_quantity(self):

        qty = self.wait.until(
            EC.visibility_of_element_located(
                self.QUANTITY
            )
        )

        return qty.get_attribute("value")

    # =========================
    # REMOVE PRODUCT
    # =========================

    def remove_product(self):

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                self.REMOVE_CHECKBOX
            )
        )

        checkbox.click()

        update = self.wait.until(
            EC.element_to_be_clickable(
                self.UPDATE_CART
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            update
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMPTY_CART_MESSAGE
            )
        )

    # =========================
    # CLEAR CART
    # =========================

    def clear_cart(self):
    self.driver.get("https://demowebshop.tricentis.com/cart")

    while True:
        try:
            checkbox = self.driver.find_element(*self.REMOVE_CHECKBOX)
            checkbox.click()
            self.driver.find_element(*self.UPDATE_CART).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.EMPTY_CART_MESSAGE)
            )
        except Exception:
            break   # no more checkboxes left = cart is fully empty
            
        except Exception:

            pass

    

    # =========================
    # COUPON
    # =========================

    def enter_coupon(self, coupon):

        # Open cart page
        self.driver.get(
            "https://demowebshop.tricentis.com/cart"
        )

        # Wait for coupon textbox
        box = self.wait.until(
            EC.presence_of_element_located(
                self.COUPON_BOX
            )
        )

        # Scroll to coupon section
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            box
        )

        # Enter coupon
        box.clear()
        box.send_keys(coupon)

        # Click Apply Coupon
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.APPLY_COUPON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        return True

    # =========================
    # GIFT CARD
    # =========================

    def is_gift_card_section_displayed(self):

        self.driver.get(
            "https://demowebshop.tricentis.com/cart"
        )

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.GIFT_CARD_TEXT
                )
            )

            return True

        except Exception:

            return False

    # =========================
    # EMPTY CART MESSAGE
    # =========================

    def get_empty_cart_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.EMPTY_CART_MESSAGE
            )
        ).text
