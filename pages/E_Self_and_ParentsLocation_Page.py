import random

from selenium.webdriver.common.by import By

from pages.D_Plan_To_Opt_Floater import PlanToOptPage
from utilities.explicit_wait_class import explicit_wait
from utilities.excel_file_read_data import read_excel_data5
from utilities.custorms_actions_chains import CustomActionChains


class SelfParentsLocationPage(PlanToOptPage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger = logger
        self.custom_action_class = CustomActionChains(self.driver)

    def entering_self_city_location(self):
        self.logger.info(f"plan opted get selected")
        plant_opted = PlanToOptPage(self.driver, self.logger)
        plant_opted.selecting_plan_to_opt_family_floater()

        enter_self_pin_or_city = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-location']"), 'clickable', 10)

        returned_data = read_excel_data5("Cities", "self_cities")
        self_city_name = random.choice(returned_data)
        self_city_to_send = self_city_name
        self.logger.debug(f"randomly choosing the self city name from the excel file")
        self.custom_action_class.send_keys_to_element(enter_self_pin_or_city, self_city_to_send)

        city_name_send_xpath = f"//h6[normalize-space() = '{self_city_to_send}']"
        city_name_sended = explicit_wait(self.driver, (By.XPATH, city_name_send_xpath), 'clickable', 10)
        city_name_sended.click()
        self.logger.debug(f"city name sended to the city box")

        # enter_self_pin_or_city.send_keys(parents_city_name)
        # self.action_class.press_enter()
        continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"),
                                        'clickable', 10)
        continue_button.click()
        self.logger.info(f"clicked on continue button")
        # self.action_class.send_keys_to_element(enter_pin_or_city,"Pune")

    def entering_parents_city_location(self):
        random_data_relation = ["Relation"]
        random_data = random.choice(random_data_relation)
        returned_data = read_excel_data5("Insurer_Relation", random_data)
        self.logger.debug(f"randomly choosing the value from the excel file")
        for row_data in returned_data:
            if row_data == "auto_father" or row_data == "auto_mother":
                self.logger.info("Checking if the randomly chosen value is Father or Mother")
                enter_parents_pin_or_city = explicit_wait(self.driver, (By.XPATH, "//input[@id='auto-location']"),
                                                          'clickable', 10)
                returned_data = read_excel_data5("Cities", "parents_cities")
                parents_city_name = random.choice(returned_data)
                parents_city_to_send = parents_city_name
                if len(parents_city_to_send) < 15 and parents_city_to_send == parents_city_name:
                    self.custom_action_class.send_keys_to_element(enter_parents_pin_or_city, parents_city_to_send)

                    if parents_city_to_send == "Bangalore" or "Delhi" or "pune" or "Mumbai" or "Gurgaon" or "Ahmedabad" or "Thane":
                        city_name_send_xpath_present = f"(//h6[normalize-space() = '{parents_city_to_send}'])[1]"
                        city_name_send = explicit_wait(self.driver, (By.XPATH, city_name_send_xpath_present),
                                                       'clickable',
                                                       10)
                        city_name_send.click()
                        continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"),
                                                        'clickable', 10)
                        continue_button.click()
                        break
                    else:
                        city_name_send_xpath = f"//h6[normalize-space() = '{parents_city_to_send}']"
                        city_name_send = explicit_wait(self.driver, (By.XPATH, city_name_send_xpath), 'clickable', 10)
                        city_name_send.click()
                        continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"),
                                                        'clickable', 10)
                        continue_button.click()
        else:
            print("Parents not selected as insurer")
            self.logger.warning("Parents not selected as insurer")

    def assert_tell_self_city_location(self):
        self.logger.info("Asserting Tell us where your element")
        you_live = explicit_wait(self.driver, (By.XPATH, "//h2[normalize-space(text()) = 'Tell us where your ']"),
                                 'clickable', 10)
        if you_live is not None:
            assert you_live.is_displayed(), "Tell us where your element is not displayed"

    def assert_tell_parents_city_location(self):
        self.logger.info("Asserting Father, mother element")
        your_parents_live = explicit_wait(self.driver, (By.XPATH, "//span[normalize-space()='father, mother']"),
                                          'clickable', 10)
        if your_parents_live is not None:
            assert your_parents_live.is_displayed(), "Father, mother element is not displayed"
