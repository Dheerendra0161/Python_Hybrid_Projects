from selenium import webdriver
from utilities.read_configurations import read_config
import pytest
from utilities.custom_logging import LoggerCustom


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


@pytest.fixture(scope="function")
def logger(request):

    # Get the class name dynamically
    class_name = request.cls.__name__

    # Initialize logger with append mode and include class name in the file name
    logger = LoggerCustom().setup_logger(f"{class_name}.log", 50084, 10, mode='a')

    # Log a message indicating the start of the test
    logger.info(f"************** Appended {class_name} **************************")

    # Return the logger object for the test
    yield logger

