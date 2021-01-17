from locators.login import LoginLocators


class LoginPage:
    def __init__(self, app):
        self.app = app

    def sign_button(self):
        return self.app.driver.find_element(*LoginLocators.LOGIN_BUTTON)

    def sign_button_click(self):
        self.sign_button().click()

    def _email_input(self):
        return self.app.driver.find_element(*LoginLocators.EMAIL_INPUT)

    def _password_input(self):
        return self.app.driver.find_element(*LoginLocators.PASSWORD_INPUT)

    def _submit_button(self):
        return self.app.driver.find_element(*LoginLocators.SUBMIT_BUTTON)

    def auth(self, email: str, password: str):
        self.sign_button_click()
        self._email_input().send_keys(email)
        self._password_input().send_keys(password)
        self._submit_button().click()
