import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    sign_in_button_xpath = "//*[text()='Sign in']"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        # assert self.get_page_title(self.dashboard_url) == self.expected_title
