from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class CustomActionChains:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def click_element(self, element: WebElement):
        self.actions.click(element).perform()

    def send_keys_to_element(self, element: WebElement, keys: str):
        self.actions.move_to_element(element).click().send_keys(keys).perform()

    def press_enter(self):
        self.actions.send_keys(Keys.ENTER).perform()

    def hover_over_element(self, element: WebElement):
        self.actions.move_to_element(element).perform()

    def drag_and_drop(self, source_element: WebElement, target_element: WebElement):
        self.actions.drag_and_drop(source_element, target_element).perform()

    def click_and_hold_element(self, element: WebElement):
        self.actions.click_and_hold(element).perform()

    def release_element(self):
        self.actions.release().perform()

    def double_click_element(self, element: WebElement):
        self.actions.double_click(element).perform()

    def context_click_element(self, element: WebElement):
        self.actions.context_click(element).perform()

    def send_keys_to_active_element(self, keys: str):
        self.actions.send_keys(Keys.NULL).perform()  # Corrected from send_keys_to_active_element(keys).perform()

    def press_page_down_and_enter(self):
        # Press Page Down key
        self.actions.send_keys(Keys.PAGE_DOWN)
        # Press Enter key
        self.actions.send_keys(Keys.ENTER)
        # Perform the combined actions
        self.actions.perform()
