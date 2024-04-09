import pytest
from pages.B_Insurance_Application_Apply_Page import InsuranceApplicationPage


class TestInsuranceApplication:
    @pytest.mark.priority(1)
    def test_send_personal_details_male(self, setup_and_teardown):
        insurance_page = InsuranceApplicationPage(setup_and_teardown)
        insurance_page.filling_mandatory_field_male()

    @pytest.mark.priority(2)
    def test_send_personal_details_female(self, setup_and_teardown):
        insurance_page = InsuranceApplicationPage(setup_and_teardown)
        insurance_page.filling_mandatory_field_female()
