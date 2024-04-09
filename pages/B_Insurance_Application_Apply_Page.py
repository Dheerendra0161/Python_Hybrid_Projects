import logging
from selenium.webdriver.common.by import By
from pages.A_Landing_Page import LandingPage
from utilities.explicit_wait_class import explicit_wait
import pytest
from utilities.generate_fake_testdata import generate_fake_data
from utilities.custom_logging import LoggerCustom


class InsuranceApplicationPage(LandingPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = LoggerCustom().setup_logger("InsuranceApplicationPage.log", 5084, 10)  # Initialize logger for InsuranceApplicationPage

    @pytest.mark.priority(1)
    def filling_mandatory_field_male(self):
        self.logger.info("Filling mandatory fields for male applicant")
        landing_page = LandingPage(self.driver)
        landing_page.click_health_element()
        self.logger.info("Successfully clicked on health element")
        male_fake_data = generate_fake_data(gender="male")

        full_name = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-fullName']"), 'visibility', 20)
        full_name.send_keys(male_fake_data["full_name"])
        self.logger.debug(f"Entered full name: {male_fake_data['full_name']}")

        mobile_number = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-mobile']"), 'visibility', 20)
        mobile_number.send_keys(male_fake_data["mobile_number"])
        self.logger.debug(f"Entered mobile number: {male_fake_data['mobile_number']}")

        email_id = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-email']"), 'visibility', 20)
        email_id.send_keys(male_fake_data["email"])
        self.logger.debug(f"Entered email: {male_fake_data['email']}")

        get_started = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-getStarted']"), 'clickable', 20)
        get_started.click()
        self.logger.info("Clicked on Get Started button")

    @pytest.mark.priority(2)
    def filling_mandatory_field_female(self):
        self.logger.info("Filling mandatory fields for female applicant")
        landing_page = LandingPage(self.driver)
        landing_page.click_health_element()
        female_fake_data = generate_fake_data(gender="female")

        select_gender_female = explicit_wait(self.driver, (By.XPATH, "//img[@alt='Female']"), 'clickable', 20)
        select_gender_female.click()
        self.logger.debug("Selected Female gender")

        full_name = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-fullName']"), 'visibility', 20)
        full_name.send_keys(female_fake_data["full_name"])
        self.logger.debug(f"Entered full name: {female_fake_data['full_name']}")

        mobile_number = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-mobile']"), 'visibility', 20)
        mobile_number.send_keys(female_fake_data["mobile_number"])
        self.logger.debug(f"Entered mobile number: {female_fake_data['mobile_number']}")

        email_id = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-email']"), 'visibility', 20)
        email_id.send_keys(female_fake_data["email"])
        self.logger.debug(f"Entered email: {female_fake_data['email']}")

        get_started = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-getStarted']"), 'clickable', 20)
        get_started.click()
        self.logger.info("Clicked on Get Started button")
