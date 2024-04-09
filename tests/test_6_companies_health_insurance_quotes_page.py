import pytest
from pages.F_Companies_Health_Insurance_Quotes_Page import CompaniesHealthInsuranceQuotesPage


class TestHealthInsuranceOpted:
    @pytest.mark.priority(1)
    def test_selecting_insurance_plan_company(self, setup_and_teardown):
        choose_health_insurance_company = CompaniesHealthInsuranceQuotesPage(setup_and_teardown)
        choose_health_insurance_company.assert_edit_details_button()
        choose_health_insurance_company.choose_insurer_companies_plan()
        choose_health_insurance_company.assert_review_your_cart_before_proceed_popup_page()
        choose_health_insurance_company.continue_button_method()




