from locators.my_credit_slips import MyCreditSlipsLocators


class MyCreditSlipsPage:
    def __init__(self, app):
        self.app = app

    def my_credit_slips_button(self):
        return self.app.driver.find_element(*MyCreditSlipsLocators.CREDIT_SLIPS_BUTTON)

    def my_credit_slips_button_click(self):
        self.my_credit_slips_button().click()

    def check(self):
        """
        Функция которая кликает по кнопке 'my credit slips',
        добавлена для читабельности теста
        """
        self.my_credit_slips_button_click()

    def my_c_s_field(self):
        return self.app.driver.find_element(*MyCreditSlipsLocators.CREDIT_SLIPS_TEXT)

    def my_c_s_field_text(self):
        return self.my_c_s_field().text
