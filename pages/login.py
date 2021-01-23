from locators.login import LoginLocators


class LoginPage:
    def __init__(self, app):
        self.app = app

    def sign_button(self):
        return self.app.driver.find_element(*LoginLocators.LOGIN_BUTTON)

    def sign_button_click(self):
        self.sign_button().click()

    def sign_button_get_text(self):
        return self.sign_button().text

    def _email_input(self):
        return self.app.driver.find_element(*LoginLocators.EMAIL_INPUT)

    def _password_input(self):
        return self.app.driver.find_element(*LoginLocators.PASSWORD_INPUT)

    def _submit_button(self):
        return self.app.driver.find_element(*LoginLocators.SUBMIT_BUTTON)

    def auth(self, email: str, password: str):
        self.sign_button_click()
        if email is not None:
            self._email_input().send_keys(email)
        if password is not None:
            self._password_input().send_keys(password)
        self._submit_button().click()

    def logout_button(self):
        return self.app.driver.find_element(*LoginLocators.LOGOUT_BUTTON)

    def logout_button_click(self):
        self.logout_button().click()

    def get_userdata(self):
        return self.app.driver.find_element(*LoginLocators.LOGIN_BUTTON).text

    def login_auth_alert(self):
        return self.app.driver.find_element(*LoginLocators.ALERT)

    def login_auth_alert_get_text(self):
        return self.login_auth_alert().text

