import pytest

from utils.excel_reader import get_login_data
from pages.login_page import LoginPage
from utils.config import BASE_URL


@pytest.mark.parametrize(
    "email,password,expected",
    get_login_data()
)
def test_login(driver, email, password, expected):

    # ==========================
    # OPEN WEBSITE
    # ==========================

    driver.get(BASE_URL)

    print("Website opened")


    # ==========================
    # LOGIN
    # ==========================

    login = LoginPage(driver)

    login.login(
        email,
        password
    )


    # ==========================
    # VERIFY LOGIN RESULT
    # ==========================

    if expected == "Pass":

        assert login.is_login_successful()

        print("Login successful")


    else:

        assert not login.is_login_successful()

        print("Login failed as expected")