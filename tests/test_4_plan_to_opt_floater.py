import pytest
from pages.D_Plan_To_Opt_Floater import PlanToOptPage


class TestPlanToOpt:
    @pytest.mark.priority(1)
    def test_selecting_plan_to_opt_family_floater(self, setup_and_teardown):
        plant_opted = PlanToOptPage(setup_and_teardown)
        plant_opted.selecting_plan_to_opt_family_floater()

    @pytest.mark.priority(2)
    def test_selecting_plan_to_opt_multi_individual(self, setup_and_teardown):
        plant_opted = PlanToOptPage(setup_and_teardown)
        plant_opted.selecting_plan_to_opt_multi_individual()
