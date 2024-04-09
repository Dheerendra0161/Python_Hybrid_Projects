import random
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.F_Companies_Health_Insurance_Quotes_Page import ChooseMultiYearOptionsAndReviewCartPage
from utilities.explicit_wait_class import explicit_wait

from utilities.custom_logging import LoggerCustom


class HealthInsuranceOptionPage():
    def __init__(self, driver):
        super().__init__(driver)

    def choose_insurer_company(self):
        yearly_plan = explicit_wait(self.driver, (
            By.XPATH, "//div[@id='auto-edelweiss_general']//h6[contains(@class,'typography--variant-subheading2')]"),
                                    'clickable', 10)
        yearly_plan.click()

    def cart_review_button(self):
        cart_review = explicit_wait(self.driver, (By.XPATH, "// h5[ @ id = 'auto-continueCTA']"),
                                    'clickable', 10)
        cart_review.click()
