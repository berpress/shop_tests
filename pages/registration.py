from locators.registration import RegistrationLocators
from time import time


class RegistrationPage:
    def __init__(self, app):
        self.app = app

    def wrong_email_alert(self, wait_time=5):
        timestamp = time() + wait_time
        while time() < timestamp:
            element = self.app.driver.find_element(*RegistrationLocators.WRONG_EMAIL_ALERT).text
        return element

    def sign_in_header_button(self):
        return self.app.driver.find_element(*RegistrationLocators.SIGN_IN_BUTTON)

    def email_field(self):
        return self.app.driver.find_element(*RegistrationLocators.EMAIL_CREATE)

    def create_account_button(self):
        return self.app.driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON)

    def heading(self):
        return self.app.driver.find_element(*RegistrationLocators.HEADING)

    def mr_radiobutton(self):
        return self.app.driver.find_element(*RegistrationLocators.MR_RADIOBUTTON)

    def mrs_radiobutton(self):
        return self.app.driver.find_element(*RegistrationLocators.MRS_RADIOBUTTON)

    def firstname(self):
        return self.app.driver.find_element(*RegistrationLocators.FIRSTNAME)

    def lastname(self):
        return self.app.driver.find_element(*RegistrationLocators.LASTNAME)

    def email(self):
        return self.app.driver.find_element(*RegistrationLocators.EMAIL)

    def passwd(self):
        return self.app.driver.find_element(*RegistrationLocators.PASSWD)

    def days(self):
        return self.app.driver.find_element(*RegistrationLocators.DAYS)

    def months(self):
        return self.app.driver.find_element(*RegistrationLocators.MONTHS)

    def years(self):
        return self.app.driver.find_element(*RegistrationLocators.YEARS)

    def newsletter_checkbox(self):
        return self.app.driver.find_element(*RegistrationLocators.NEWSLETTER_CHECKBOX)

    def optin_checkbox(self):
        return self.app.driver.find_element(*RegistrationLocators.OPTIN_CHECKBOX)

    def first_name(self):
        return self.app.driver.find_element(*RegistrationLocators.FIRST_NAME)

    def last_name(self):
        return self.app.driver.find_element(*RegistrationLocators.LAST_NAME)

    def company(self):
        return self.app.driver.find_element(*RegistrationLocators.COMPANY)

    def address_line1(self):
        return self.app.driver.find_element(*RegistrationLocators.ADDRESS_LINE1)

    def address_line2(self):
        return self.app.driver.find_element(*RegistrationLocators.ADDRESS_LINE2)

    def city(self):
        return self.app.driver.find_element(*RegistrationLocators.CITY)

    def state(self):
        return self.app.driver.find_element(*RegistrationLocators.STATE)

    def postal_code(self):
        return self.app.driver.find_element(*RegistrationLocators.POSTAL_CODE)

    def country(self):
        return self.app.driver.find_element(*RegistrationLocators.COUNTRY)

    def additional_info(self):
        return self.app.driver.find_element(*RegistrationLocators.ADDITIONAL_INFO)

    def home_phone(self):
        return self.app.driver.find_element(*RegistrationLocators.HOME_PHONE)

    def mobile_phone(self):
        return self.app.driver.find_element(*RegistrationLocators.MOBILE_PHONE)

    def address_alias(self):
        return self.app.driver.find_element(*RegistrationLocators.ADDRESS_ALIAS)

    def register_button(self):
        return self.app.driver.find_element(*RegistrationLocators.REGISTER_BUTTON)

    def errors(self):
        return self.app.driver.find_element(*RegistrationLocators.ERRORS).text

    def account_header(self):
        return self.app.driver.find_element(*RegistrationLocators.ACCOUNT_HEADER).text

    def go_to_registration_form(self, email):
        self.sign_in_header_button().click()
        self.email_field().send_keys(email)
        self.create_account_button().click()

    def fill_personal_information(self, passwd, firstname, lastname, years):
        """Заполнение секции Your personal information"""
        self.app.driver.implicitly_wait(10)
        self.mrs_radiobutton().click()
        self.firstname().send_keys(firstname)
        self.lastname().send_keys(lastname)
        self.passwd().send_keys(passwd)
        self.days().send_keys("13")
        self.months().send_keys("January")
        self.years().send_keys(years)
        self.newsletter_checkbox().click()
        self.optin_checkbox().click()

    def fill_address(self, first_name, last_name, address, city, country, phone):
        """Заполнение секции Your address"""
        self.first_name().send_keys(first_name)
        self.last_name().send_keys(last_name)
        self.company().send_keys("blah")
        self.address_line1().send_keys(address)
        self.address_line2().send_keys("blah")
        self.city().send_keys(city)
        self.state().send_keys("Iowa")
        self.postal_code().send_keys("45212")
        self.country().send_keys(country)
        self.additional_info().send_keys("blah")
        self.home_phone().send_keys(phone)
        self.mobile_phone().send_keys(phone)
        self.address_alias().send_keys("blah")
        self.register_button().click()
