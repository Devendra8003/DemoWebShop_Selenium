import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
