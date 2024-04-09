import random
import time
from datetime import datetime, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.B_Insurance_Application_Apply_Page import InsuranceApplicationPage
from utilities.explicit_wait_class import explicit_wait
from utilities.excel_file_read_data import read_excel_data, read_excel_data3, read_excel_data5
from utilities.generate_age_data import generate_age_data
from utilities.custorms_actions_chains import ActionChains, CustomActionChains


class WhomToInsurePage(InsuranceApplicationPage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.logger = logger
        self.action_class = ActionChains(self.driver)

    def selecting_member_to_insured(self):
        insurance_page = InsuranceApplicationPage(self.driver, self.logger)
        insurance_page.filling_mandatory_field_male()
        global spouse_age, daughter_age, son_age, father_age, mother_age, spouse_age, son_age, daughter_age, self_age
        father_age = None
        self_age = None

        # excel_sheet_name = ['Relations', 'Relations1', 'Relations2', 'Relations3', 'Relations4', 'Relations5']
        # relation = random.choice(excel_sheet_name)

        # returned_data, max_columns = read_excel_data3("Insurer_Relation", 'random')  # Request random column
        # column_number = random.randint(1, 7)  # Random column number between 1 and max_columns
        # returned_data, max_columns = read_excel_data3("Insurer_Relation", column_number)

        random_data_relation = ["Relation6", "Relation3", "Relation4", "Relation5"]
        random_data = random.choice(random_data_relation)
        returned_data = read_excel_data5("Insurer_Relation", random_data)
        self.logger.debug(f"random data of relation get selected")
        for row_data in returned_data:
            self.logger.info(f"row_data {row_data} sends to dynamic xpath relations and age")
            select_relation = f"//div[@id='{row_data}']/section/button"
            select_age = f"//div[@id='{row_data}']/section/div/div/div/div[contains(text(),'Select Age')]/parent::div"

            select_member_relation = explicit_wait(self.driver, (By.XPATH, select_relation), 'clickable', 20)
            select_member_relation.click()
            self.logger.debug(f"selected member get clicked")
            select_member_age = explicit_wait(self.driver, (By.XPATH, select_age), 'clickable', 20)
            self.action_class.click(select_member_age).perform()
            self.logger.debug(f"selected member age get clicked")
            if "auto_spouse" in row_data:
                test_data = generate_age_data("spouse")
            elif "auto_son" in row_data:
                # If son, check if age is "Below 3 months"
                age_data = generate_age_data("son")

                if age_data == "Below 3 months":
                    test_data = age_data
                    self.logger.debug(f"test_data selected from the age data is below 3 months ")
                    self.action_class.send_keys(str(test_data)).send_keys(Keys.ENTER).perform()
                    # DOB within the last 3 months
                    dob = datetime.now() - timedelta(days=random.randint(1, 90))
                    dob_test_data = dob.strftime("%d-%m-%Y")
                    son_dob_input = explicit_wait(self.driver, (By.XPATH, "//input[@id=':r8:']"), 'clickable', 10)
                    self.action_class.send_keys_to_element(son_dob_input, dob_test_data)
                    time.sleep(2)
                else:
                    test_data = age_data
            elif "auto_daughter" in row_data:
                # If daughter, check if age is "Below 3 months"
                age_data = generate_age_data("daughter")
                if age_data == "Below 3 months":
                    dob = datetime.now() - timedelta(days=random.randint(1, 90))
                    test_data = dob.strftime("%d-%m-%Y")
                    daughter_dob_input = explicit_wait(self.driver, (By.XPATH, "//input[@id=':r9:']"), 'clickable', 10)
                    self.action_class.send_keys_to_element(daughter_dob_input, test_data)
                    time.sleep(2)
                else:
                    test_data = age_data
            elif "auto_father" in row_data or "auto_mother" in row_data:
                test_data = generate_age_data("father")
            else:
                test_data = generate_age_data("self")

            self.action_class.send_keys(str(test_data)).send_keys(Keys.ENTER).perform()
            self.logger.debug(f" send the keys to the required fields")

            # Check if it's father or self and save the age
            try:
                if "auto_father" in row_data:
                    father_age = test_data
                if "auto_mother" in row_data:
                    mother_age = test_data
                if "auto_spouse" in row_data:
                    spouse_age = test_data
                if "auto_son" in row_data:
                    son_age = test_data
                if "auto_daughter" in row_data:
                    daughter_age = test_data

                if "auto_self" in row_data:
                    self_age = test_data

                # Check for minimum age gaps
                if father_age is not None and self_age is not None and abs(father_age - self_age) < 18:
                    raise ValueError("Minimum age gap between Self and Father should be greater than 18 years.")
                if mother_age is not None and self_age is not None and abs(mother_age - self_age) < 18:
                    raise ValueError("Minimum age gap between Self and Mother should be greater than 18 years.")
                if spouse_age is not None and son_age is not None and abs(spouse_age - son_age) < 18:
                    raise ValueError("Minimum age gap between Spouse and Son should be 18 years.")
                if spouse_age is not None and daughter_age is not None and abs(spouse_age - daughter_age) < 18:
                    raise ValueError("Minimum age gap between Spouse and Daughter should be 18 years.")
                if self_age is not None and son_age is not None and abs(self_age - son_age) < 18:
                    raise ValueError("Minimum age gap between Self and Son should be 18 years.")
                if self_age is not None and daughter_age is not None and abs(self_age - daughter_age) < 18:
                    raise ValueError("Minimum age gap between Self and Daughter should be 18 years.")

                # Perform actions if all conditions are met
                if (father_age is not None and
                        self_age is not None and
                        mother_age is not None and
                        spouse_age is not None and
                        son_age is not None and
                        daughter_age is not None and
                        abs(spouse_age - son_age) < 18 and
                        abs(spouse_age - daughter_age) < 18 and
                        abs(mother_age - self_age) < 18 and
                        abs(father_age - self_age) < 18 and
                        abs(self_age - daughter_age) < 18 and
                        abs(self_age - daughter_age) < 18):
                    # Add 18 years to ages
                    if (abs(spouse_age - son_age) < 18 and abs(spouse_age - daughter_age) < 18):
                        test_data_spouse = spouse_age + 18
                        self.action_class.send_keys(str(test_data_spouse)).send_keys(Keys.ENTER).perform()

                    if (abs(mother_age - self_age) < 18 and abs(father_age - self_age) < 18):
                        test_data_father = father_age + 18
                        test_data_mother = mother_age + 18
                        self.action_class.send_keys(str(test_data_father)).send_keys(Keys.ENTER).perform()
                        self.action_class.send_keys(str(test_data_mother)).send_keys(Keys.ENTER).perform()
                    if (abs(self_age - daughter_age) < 18 and abs(self_age - daughter_age) < 18):
                        test_data_self = self_age + 18
                        self.action_class.send_keys(str(test_data_self)).send_keys(Keys.ENTER).perform()

                    # Click continue button
                    # continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"),
                    #                                 'clickable', 20)
                    continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"),
                                                    'clickable', 20)
                    # continue_button.click()

                    # self.action_class.click(continue_button).perform()
                    # CustomActionChains.click_element(self.driver, continue_button)

            except ValueError as ve:
                print(f"ValueError: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")

        continue_button = explicit_wait(self.driver, (By.XPATH, "//h4[@id='auto-Continue']"),
                                        'clickable', 20)
        continue_button.click()
        self.logger.info(f"clicked on the continue button")
        # CustomActionChains.click_element(self.driver, continue_button)
# Use it   # Perform the action for all cases except when age is "Below 3 months" for sons and daughters
#             if not (("auto_son" in row_data or "auto_daughter" in row_data) and test_data == "Below 3 months"):
#                 self.action_class.send_keys(str(test_data)).send_keys(Keys.ENTER).perform()
#
#             # Check if it's father or self and save the age
