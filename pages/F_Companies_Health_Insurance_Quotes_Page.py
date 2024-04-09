import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.E_Self_and_ParentsLocation_Page import SelfParentsLocationPage
from utilities.custorms_actions_chains import CustomActionChains
from utilities.explicit_wait_class import explicit_wait, explicit_wait_elements
from utilities.java_script_executor import scroll_into_view
from utilities.custom_logging import LoggerCustom


class CompaniesHealthInsuranceQuotesPage(SelfParentsLocationPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.custom_action_class = CustomActionChains(self.driver)
        self.logger = LoggerCustom().setup_logger("CompaniesHealthInsuranceQuotesPage.log", 5084, 10)

    def assert_edit_details_button(self):
        self.logger.info("Asserting Edit Details Button")
        edit_details_button = explicit_wait(self.driver, (
            By.XPATH, "//h6[normalize-space() = 'Edit Details']"), 'presence', 25)
        if edit_details_button is not None:
            assert edit_details_button.is_displayed(), "edit details button not displayed"

    def choose_insurer_companies_plan(self):
        self.logger.info("Choosing Insurer Companies Plan")
        location_value = SelfParentsLocationPage(self.driver)
        location_value.assert_tell_self_city_location()
        location_value.entering_self_city_location()
        location_value.assert_tell_parents_city_location()
        location_value.entering_parents_city_location()

        yearly_premium_button_options_elements = explicit_wait_elements(self.driver, (
            By.XPATH, "//div[@class='sc-eEbqID FvKNZ']/descendant::div[@class='sc-ghzrUh iJNwfU']/child::a/div"
        ), 'clickable', 25)

        try:
            if len(yearly_premium_button_options_elements) >= 1:
                random_element = random.choice(yearly_premium_button_options_elements)
                ran_ele = random_element
                scroll_into_view(self.driver, ran_ele)
                self.custom_action_class.click_element(ran_ele)
                # self.custom_action_class.hover_over_element(ran_ele)
                # ran_ele.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            self.logger.error(f"Element not found: {e}")

        # yearly_premium_button = explicit_wait(self.driver, (By.XPATH, "//div[@id='auto-edelweiss_general']"),
        #                                       'clickable', 25)
        # self.custom_action_class.hover_over_element(yearly_premium_button)
        # yearly_premium_button.click()

    def assert_review_your_cart_before_proceed_popup_page(self):
        self.logger.info("Asserting Review Your Cart Popup Page")
        review_your_cart = explicit_wait(self.driver, (
            By.XPATH,
            "//h5[contains(text(),'take a minute and review your cart bef')]"),
                                         'presence', 10)
        if review_your_cart is not None:
            assert review_your_cart.is_displayed(), "take a minute and review your cart before you proceed not displayed"

    def continue_button_method(self):
        self.logger.info("Clicking Continue Button")
        continue_button = explicit_wait(self.driver, (
            By.XPATH, "//h5[@id='auto-continueCTA']|//h5[text()='Continue']"), 'clickable', 10)
        self.custom_action_class.click_element(continue_button)
        self.logger.debug("Clicked on Continue button")
        # click_continue.click()


class ChooseMultiYearOptionsAndReviewCartPage:
    pass