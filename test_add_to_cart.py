from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_add_to_cart(driver):

    # Open Books category
    books = driver.find_element(By.LINK_TEXT, "Books")

    actions = ActionChains(driver)
    actions.move_to_element(books).click().perform()

    # Click first Add to Cart button
    add_to_cart = driver.find_element(
        By.CSS_SELECTOR,
        "input[value='Add to cart']"
    )

    ActionChains(driver).move_to_element(add_to_cart).click().perform()

    print("Product Added Successfully")