from pages.A_Landing_Page import LandingPage


class TestLanding:
    # def test_verify_health_element(self, setup_and_teardown):
    #     landing_page = LandingPage(setup_and_teardown)
    #     assert landing_page.verify_health_element()

    def test_click_on_health_element(self, setup_and_teardown):
        landing_page = LandingPage(setup_and_teardown)
        landing_page.click_health_element()
