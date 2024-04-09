from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def explicit_wait(driver, locator, wait_type="", timeout=10):
    try:
        if wait_type == "visibility":
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        elif wait_type == "presence":
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        elif wait_type == "clickable":
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        else:
            raise ValueError("Invalid wait type. Use 'visibility', 'presence', or 'clickable'.")
        return element

    except Exception as e:
        print(f"Error waiting for element: {e}")
        return None


def explicit_wait_elements(driver, locator, wait_type="", timeout=10):
    try:
        if wait_type == "visibility":
            elements = WebDriverWait(driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        elif wait_type == "presence":
            elements = WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        elif wait_type == "clickable":
            elements = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        else:
            raise ValueError("Invalid wait type. Use 'visibility', 'presence', or 'clickable'.")
        return elements

    except Exception as e:
        print(f"Error waiting for elements: {e}")
        return []


def explicit_wait_web_element(driver, webelement, wait_type="", timeout=10):
    try:
        if wait_type == "visibility":
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of(webelement)
            )
        elif wait_type == "presence":
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(webelement)
            )
        elif wait_type == "clickable":
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(webelement)
            )
        else:
            raise ValueError("Invalid wait type. Use 'visibility', 'presence', or 'clickable'.")
        return element

    except Exception as e:
        print(f"Error waiting for element: {e}")
        return None
