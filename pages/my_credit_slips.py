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
        Функция которая кликает по кнопке 'my_orders info',
        добавлена для читабельности теста
        """
        self.my_credit_slips_button_click()
