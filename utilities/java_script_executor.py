from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def execute_script(driver, script, *args):
    try:
        result = driver.execute_script(script, *args)
        return result
    except Exception as e:
        print(f"Error executing script: {e}")
        return None


def scroll_into_view(driver, element):
    script = "arguments[0].scrollIntoView();"
    execute_script(driver, script, element)


def click_element_js(driver, element):
    script = "arguments[0].click();"
    execute_script(driver, script, element)


def set_attribute(driver, element, attribute, value):
    script = "arguments[0].setAttribute(arguments[1], arguments[2]);"
    execute_script(driver, script, element, attribute, value)


def get_attribute(driver, element, attribute):
    script = "return arguments[0].getAttribute(arguments[1]);"
    return execute_script(driver, script, element, attribute)


def remove_attribute(driver, element, attribute):
    script = "arguments[0].removeAttribute(arguments[1]);"
    execute_script(driver, script, element, attribute)


def scroll_to_bottom(driver):
    script = "window.scrollTo(0, document.body.scrollHeight);"
    execute_script(driver, script)


def scroll_to_top(driver):
    script = "window.scrollTo(0, 0);"
    execute_script(driver, script)


def highlight_element(driver, element):
    script = "arguments[0].style.border = '2px solid red';"
    execute_script(driver, script, element)


def unhighlight_element(driver, element):
    script = "arguments[0].style.border = ''"
    execute_script(driver, script, element)


def get_page_title(driver):
    script = "return document.title;"
    return execute_script(driver, script)


def get_page_url(driver):
    script = "return document.URL;"
    return execute_script(driver, script)
