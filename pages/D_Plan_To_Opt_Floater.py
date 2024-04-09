from selenium.webdriver.common.by import By
from utilities.explicit_wait_class import explicit_wait
from pages.C_Whom_To_Insure_Page import WhomToInsurePage


class PlanToOptPage(WhomToInsurePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger = logger

    def selecting_plan_to_opt_family_floater(self):
        person_insured = WhomToInsurePage(self.driver, self.logger)
        person_insured.selecting_member_to_insured()
        family_floater = explicit_wait(self.driver, (By.XPATH, "//span[@id='auto_F']"),
                                       'clickable', 10)
        family_floater.click()
        self.logger.debug(f"family floater option selected and  clicked")
        continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"), 'clickable', 10)
        continue_button.click()
        self.logger.info(f"continue button clicked")

    def selecting_plan_to_opt_multi_individual(self):
        person_insured = WhomToInsurePage(self.driver, self.logger)
        person_insured.selecting_member_to_insured()
        multi_individual = explicit_wait(self.driver, (By.XPATH, "//span[@id='auto_M']"),
                                         'clickable', 10)
        multi_individual.click()
        self.logger.debug(f"multi individual option selected and  clicked")
        continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"), 'clickable', 10)
        continue_button.click()
        self.logger.info(f"continue button clicked")
