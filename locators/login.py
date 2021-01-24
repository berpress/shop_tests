from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, 'header_user_info')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'passwd')
    SUBMIT_BUTTON = (By.ID, 'SubmitLogin')
    LOGOUT_BUTTON = (By.CLASS_NAME, 'logout')
    ALERT = (By.XPATH, '//*[@class="alert alert-danger"]')

