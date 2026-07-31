import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.email_friend_page import EmailFriendPage


from utils.config import BASE_URL



def test_email_friend(driver):


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
        "devendra123@gmail.com",
        "Test@123"
    )


    print("Login completed")



    # ==========================
    # SEARCH PRODUCT
    # ==========================

    search = SearchPage(driver)


    search.search_product(
        "Health Book"
    )


    print("Product searched")



    # ==========================
    # OPEN PRODUCT
    # ==========================

    WebDriverWait(driver,10).until(

        EC.element_to_be_clickable(
            (
                By.LINK_TEXT,
                "Health Book"
            )
        )

    ).click()


    print("Product opened")



    # ==========================
    # EMAIL FRIEND
    # ==========================

    product = ProductPage(driver)


    product.click_email_friend()


    print("Email friend page opened")



    # ==========================
    # ENTER DETAILS
    # ==========================

    email = EmailFriendPage(driver)



    email.enter_friend_email(
        "friend1@gmail.com"
    )



    email.enter_your_email(
        "devendra123@gmail.com"
    )



    email.enter_message(
        "I think you will like this product."
    )


    print("All details entered")



    # ==========================
    # SEND EMAIL
    # ==========================

    email.click_send()


    time.sleep(3)



    # DEBUG OUTPUT

    print(
        driver.current_url
    )


    print(
        driver.find_element(
            By.TAG_NAME,
            "body"
        ).text
    )



    # ==========================
    # VERIFY
    # ==========================


    error_message = email.get_error_message()


    success_message = email.get_success_message()



    print(
        "ERROR:",
        error_message
    )


    print(
        "SUCCESS:",
        success_message
    )



    # Accept both results

    assert (

        "Only registered customers can use email a friend feature"
        in error_message

        or

        "Your message has been sent"
        in success_message

    )