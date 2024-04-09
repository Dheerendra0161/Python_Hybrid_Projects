import pytest
from pages.B_Insurance_Application_Apply_Page import InsuranceApplicationPage
from pages.A_Landing_Page import LandingPage
from pages.D_Plan_To_Opt_Floater import PlanToOptPage
from pages.E_Self_and_ParentsLocation_Page import SelfParentsLocationPage


class TestPlanToOpt:
    @pytest.mark.priority(1)
    def test_selecting_location_of_self(self, setup_and_teardown):
        location_value = SelfParentsLocationPage(setup_and_teardown)
        location_value.assert_tell_self_city_location()
        location_value.entering_self_city_location()
        location_value.assert_tell_parents_city_location()
        location_value.entering_parents_city_location()

    # @pytest.mark.priority(2)
    # def test_selecting_location_of_parents(self, setup_and_teardown):
    #     location_value = LocationPage(setup_and_teardown)
    #     location_value.assert_tell_parents_city_location()
    #     location_value.entering_parents_city_location()
