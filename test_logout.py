from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver
from utils.config import BASE_URL, EMAIL, PASSWORD

from pages.login_page import LoginPage


def test_logout():

    driver = get_driver()

    try:
        # Open website
        driver.get(BASE_URL)

        # Login
        login = LoginPage(driver)
        login.login(EMAIL, PASSWORD)

        assert login.is_login_successful()

        # Logout
        driver.find_element(By.LINK_TEXT, "Log out").click()

        print("Logout Successfully")

        # Verify logout
        assert driver.find_element(By.LINK_TEXT, "Log in").is_displayed()

        print("Login link is visible")

    finally:
        driver.quit()