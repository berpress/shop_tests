from locators.my_personal_info import MyPersonalInfoLocators


class MyPersonalInfoPage:
    def __init__(self, app):
        self.app = app

    def my_personal_info_button(self):
        return self.app.driver.find_element(
            *MyPersonalInfoLocators.PERSONAL_INFO_BUTTON
        )

    def my_personal_info_button_click(self):
        self.my_personal_info_button().click()

    def check(self):
        """Функция которая кликает по кнопке 'my_personal info',
        добавлена для читабельности теста."""
        self.my_personal_info_button_click()

    def firstname_input(self):
        return self.app.driver.find_element(*MyPersonalInfoLocators.FIRSTNAME_BUTTON)

    def lastname_input(self):
        return self.app.driver.find_element(*MyPersonalInfoLocators.LASTNAME_BUTTON)

    def get_name(self):
        return self.firstname_input().get_property("defaultValue")

    def get_lastname(self):
        return self.lastname_input().get_property("defaultValue")
