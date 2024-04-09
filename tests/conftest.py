from selenium import webdriver
from utilities.read_configurations import read_config
import pytest
from allure_pytest import plugin

@pytest.fixture(scope="function")
def setup_and_teardown():
    browser = read_config("basic_info1", "Browser")
    url = read_config("basic_info1", "URL")

    if browser is None or url is None:
        pytest.skip("Browser or URL not configured")

    # Initialize WebDriver based on the configured browser
    if browser == "CH":
        driver = webdriver.Chrome()
    elif browser == "FF":
        driver = webdriver.Firefox()
    elif browser == "ED":
        driver = webdriver.Edge()
    else:
        # Default to Chrome if browser value is not recognized
        print("Invalid browser type, defaulting to Chrome.")
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(15)

    try:
        driver.get(url)
    except Exception as e:
        print(f"Error accessing URL: {e}")
        pytest.skip("Failed to access URL")

    yield driver

    driver.quit()


