import pytest

from pages.B_Insurance_Application_Apply_Page import InsuranceApplicationPage
from pages.A_Landing_Page import LandingPage
from pages.C_Whom_To_Insure_Page import WhomToInsurePage


class TestWhomToInsure:
    @pytest.mark.priority(1)
    def test_selecting_member_to_insured_male_customer(self, setup_and_teardown):

        person_insured = WhomToInsurePage(setup_and_teardown)
        person_insured.selecting_member_to_insured()

    @pytest.mark.priority(2)
    def test_selecting_member_to_insured_female_customer(self, setup_and_teardown):

        person_insured = WhomToInsurePage(setup_and_teardown)
        person_insured.selecting_member_to_insured()






