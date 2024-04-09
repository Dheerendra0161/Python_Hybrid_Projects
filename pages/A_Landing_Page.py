from selenium.webdriver.common.by import By
from utilities.explicit_wait_class import explicit_wait
from utilities.custom_logging import LoggerCustom


class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = LoggerCustom().setup_logger("LandingPage.log", 5084, 10)  # Initialize logger for LandingPage

    def click_health_element(self):
        self.logger.info("Click on health element")
        health_element = explicit_wait(self.driver, (By.XPATH, "//span[contains(text(),'Health')]"), 'clickable', 10)
        if health_element:
            health_element.click()
            self.logger.info("Successfully clicked on health element")
        else:
            self.logger.warning("Health element is not clickable")

    # Switch to new window
    # all_window_handles = self.driver.window_handles
    # new_window_handle = all_window_handles[-1]
    # self.driver.switch_to.window(new_window_handle)
