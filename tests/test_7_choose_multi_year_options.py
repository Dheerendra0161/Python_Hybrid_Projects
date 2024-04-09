import pytest

from pages.G_Your_Cart_And_Product_Details_Page import ChooseMultiYearOptionsAndReviewCartPage


class TestChooseMultiYearsAndReviewCart:
    @pytest.mark.priority(1)
    def test_selecting_insurance_plan_company(self, setup_and_teardown):
        choose_multi_years = ChooseMultiYearOptionsAndReviewCartPage(setup_and_teardown)
        choose_multi_years.choose_multi_year_options()
        choose_multi_years.review_your_cart()







