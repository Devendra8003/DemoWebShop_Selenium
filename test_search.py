from selenium.webdriver.common.by import By

def test_search(driver):
    driver.find_element(By.ID, "small-searchterms").send_keys("book")
    driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

    print("Search Successfully")