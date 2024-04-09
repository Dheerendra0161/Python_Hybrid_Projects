import random

from selenium.webdriver.common.by import By
from utilities.explicit_wait_class import explicit_wait
from utilities.excel_file_read_data import read_excel_data5
from utilities.custorms_actions_chains import CustomActionChains


class WhoToInsurePage:
    def __init__(self, driver):
        self.driver = driver
        self.action_class = CustomActionChains(self.driver)

    def selecting_member_to_insured(self):
        relation = ['Relation1', "Relation2", "Relation3", "Relation4", "Relation5"]
        current_relation = random.choice(relation)

        returned_data = read_excel_data5("Insurer_Relation", current_relation)

        # Generate a random row number between 1 and 29 (inclusive)
        row_number = random.randint(1, 29)
        # Get the data for all relation types at the specified row number
        age_row_data = {
            "self_data": read_excel_data5("Age", "self")[row_number],
            "spouse_data": read_excel_data5("Age", "spouse")[row_number],
            "son_data": read_excel_data5("Age", "son")[row_number],
            "daughter_data": read_excel_data5("Age", "daughter")[row_number],
            "father_data": read_excel_data5("Age", "father")[row_number],
            "mother_data": read_excel_data5("Age", "mother")[row_number]
        }

        for row_data in returned_data:
            if "self_data" in age_row_data and row_data == "auto_self":
                select_relation = f"//div[@id='{row_data}']/section/button"
                select_member_relation = explicit_wait(self.driver, (By.XPATH, select_relation), 'clickable', 20)
                select_member_relation.click()
                select_age = f"//div[@id='{row_data}']/section/div/div/div/div[contains(text(),'Select Age')]/parent::div"
                select_member_age = explicit_wait(self.driver, (By.XPATH, select_age), 'clickable', 20)
                self.action_class.send_keys_to_element(select_member_age, 63)  # str(age_row_data["self_data"]))
                self.action_class.click_element(select_member_age)
            # elif "spouse_data" in age_row_data and row_data == "auto_spouse":
            #     select_relation = f"//div[@id='{row_data}']/section/button"
            #     select_member_relation = explicit_wait(self.driver, (By.XPATH, select_relation), 'clickable', 20)
            #     select_member_relation.click()
            #     select_age = f"//div[@id='{row_data}']/section/div/div/div/div[contains(text(),'Select Age')]/parent::div"
            #     select_member_age = explicit_wait(self.driver, (By.XPATH, select_age), 'clickable', 20)
            #     self.action_class.send_keys_to_element(select_member_age, str(age_row_data["spouse_data"]))
            #     # self.action_class.click_element(select_member_age)
            # elif "son_data" in age_row_data and row_data == "auto_son":
            #     select_relation = f"//div[@id='{row_data}']/section/button"
            #     select_member_relation = explicit_wait(self.driver, (By.XPATH, select_relation), 'clickable', 20)
            #     select_member_relation.click()
            #     select_age = f"//div[@id='{row_data}']/section/div/div/div/div[contains(text(),'Select Age')]/parent::div"
            #     select_member_age = explicit_wait(self.driver, (By.XPATH, select_age), 'clickable', 20)
            #     self.action_class.send_keys_to_element(select_member_age, str(age_row_data["son_data"]))
            #     # self.action_class.click_element(select_member_age)
            # elif "daughter_data" in age_row_data and row_data == "auto_daughter":
            #     select_relation = f"//div[@id='{row_data}']/section/button"
            #     select_member_relation = explicit_wait(self.driver, (By.XPATH, select_relation), 'clickable', 20)
            #     select_member_relation.click()
            #     select_age = f"//div[@id='{row_data}']/section/div/div/div/div[contains(text(),'Select Age')]/parent::div"
            #     select_member_age = explicit_wait(self.driver, (By.XPATH, select_age), 'clickable', 20)
            #     self.action_class.send_keys_to_element(select_member_age, str(age_row_data["daughter_data"]))
            #     # self.action_class.click_element(select_member_age)
            # elif "father_data" in age_row_data and row_data == "auto_father":
            #     select_relation = f"//div[@id='{row_data}']/section/button"
            #     select_member_relation = explicit_wait(self.driver, (By.XPATH, select_relation), 'clickable', 20)
            #     select_member_relation.click()
            #     select_age = f"//div[@id='{row_data}']/section/div/div/div/div[contains(text(),'Select Age')]/parent::div"
            #     select_member_age = explicit_wait(self.driver, (By.XPATH, select_age), 'clickable', 20)
            #     self.action_class.send_keys_to_element(select_member_age, str(age_row_data["father_data"]))
            #     # self.action_class.click_element(select_member_age)
            # elif "mother_data" in age_row_data and row_data == "auto_mother":
            #     select_relation = f"//div[@id='{row_data}']/section/button"
            #     select_member_relation = explicit_wait(self.driver, (By.XPATH, select_relation), 'clickable', 20)
            #     select_member_relation.click()
            #     select_age = f"//div[@id='{row_data}']/section/div/div/div/div[contains(text(),'Select Age')]/parent::div"
            #     select_member_age = explicit_wait(self.driver, (By.XPATH, select_age), 'clickable', 20)
            #     self.action_class.send_keys_to_element(select_member_age, str(age_row_data["mother_data"]))
            #     # self.action_class.click_element(select_member_age)

        # Click continue button
        continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"), 'clickable', 20)
        continue_button.click()
