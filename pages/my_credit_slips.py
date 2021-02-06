from locators.my_credit_slips import MyCreditSlipsLocators


class MyCreditSlipsPage:
    def __init__(self, app):
        self.app = app

    def credit_slips_button(self):
        return self.app.driver.find_element(*MyCreditSlipsLocators.CREDIT_SLIPS_BUTTON)

    def credit_slips_button_click(self):
        self.credit_slips_button().click()

    def header(self):
        return self.app.driver.find_element(*MyCreditSlipsLocators.CREDIT_SLIPS_TEXT)

    def my_c_s_field_text(self):
        return self.header().text
