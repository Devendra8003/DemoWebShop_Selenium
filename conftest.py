import pytest
from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


# =====================================
# SCREENSHOT ON FAILURE
# =====================================
# Automatically attaches a screenshot to the HTML report
# whenever a test fails.

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is not None:

            try:
                from pytest_html import extras

                screenshot = driver.get_screenshot_as_base64()

                extra.append(
                    extras.image(screenshot, mime_type="image/png")
                )

            except Exception:
                pass

    report.extra = extra
