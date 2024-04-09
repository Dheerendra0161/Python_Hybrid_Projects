from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.F_Companies_Health_Insurance_Quotes_Page import CompaniesHealthInsuranceQuotesPage
from utilities.explicit_wait_class import explicit_wait, explicit_wait_elements
from utilities.custom_logging import LoggerCustom


class ChooseMultiYearOptionsAndReviewCartPage(CompaniesHealthInsuranceQuotesPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = LoggerCustom().setup_logger("ChooseMultiYearOptionsAndReviewCartPage.log", 5084, 10)

    def choose_multi_year_options(self):
        self.logger.info("Choosing Multi-Year Options")
        choose_health_insurance_company = CompaniesHealthInsuranceQuotesPage(self.driver)
        choose_health_insurance_company.assert_edit_details_button()
        choose_health_insurance_company.choose_insurer_companies_plan()
        choose_health_insurance_company.assert_review_your_cart_before_proceed_popup_page()
        choose_health_insurance_company.continue_button_method()

        multi_year_option_elements = explicit_wait_elements(self.driver, (
            By.XPATH, "//div[@class='sc-erUUZj hNJquZ']/descendant::div/div"),
                                                            'clickable', 10)
        if len(multi_year_option_elements) >= 1:  # Adjust index based on your requirements
            multi_year_option_elements[2].click()  # Selecting the third element
            self.logger.debug("Selected Multi-Year Option")

    def review_your_cart(self):
        self.logger.info("Reviewing Your Cart")
        review_your_cart_button = explicit_wait(self.driver, (
            By.XPATH, "//h6[contains(text(),'Review Your Cart')]|//h6[@id='auto-review-cart-button']"),
                                                'clickable', 10)
        review_your_cart_button.click()
        self.logger.debug("Clicked Review Your Cart button")

        proceeds_to_proposal_button = explicit_wait(self.driver, (By.XPATH, "//h6[normalize-space()='Yes']"),
                                                    'clickable', 10)
        proceeds_to_proposal_button.click()
        self.logger.debug("Clicked Yes button to proceed to proposal")

        kyc_verification_proceed = explicit_wait(self.driver, (By.XPATH, "//h6[@id='auto-proceed-kyc']"),
                                                 'clickable', 10)
        kyc_verification_proceed.click()
        self.logger.debug("Clicked Proceed for KYC Verification")

    def proceeds_to_proposal(self):
        self.logger.info("Proceeding to Proposal")
        pass

    def kyc_verifications(self):
        self.logger.info("Performing KYC Verifications")
        pass
