from pages.A_Landing_Page import LandingPage
import pytest


class TestLanding:
    @pytest.mark.priority(1)
    def test_click_on_health_element(self, setup_and_teardown, logger):
        landing_page = LandingPage(setup_and_teardown, logger)
        landing_page.click_health_element()
