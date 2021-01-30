from locators.filtering_woman_page import FilterWomanLocators
from models.filtering import FilteringData


class FilteringWomenPage:
    def __init__(self, app):
        self.app = app

    def women_button(self):
        return self.app.driver.find_element(*FilterWomanLocators.WOMEN_BUTTON)

    def women_button_click(self):
        self.women_button().click()

    def filter_buttons(self):
        return self.app.driver.find_element(*FilterWomanLocators.FILTERING_BUTTONS)

    def filter_buttons_click(self):
        for elem in FilteringData.random(self.filter_buttons()):
            elem.click()

    def filter(self):
        self.women_button_click()
        self.filter_buttons()
