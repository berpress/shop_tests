from common.base import BaseClass
from common.constants import Registration
from locators.registration import RegistrationLocators
import logging


logger = logging.getLogger()


class RegistrationPage(BaseClass):
    def __init__(self, app):
        self.app = app

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

    def account_header(self):
        return self.app.driver.find_element(*RegistrationLocators.ACCOUNT_HEADER).text

    def go_to_registration_form(self, email):
        self.sign_in_header_button().click()
        self.email_field().send_keys(email)
        self.create_account_button().click()

    def fill_personal_information(self, passwd, firstname, lastname, years):
        """Заполнение секции Your personal information"""
        logger.info(
            f"Пытаемся заполнить личные данные значениями"
            f" {passwd}{firstname}{lastname}{years}"
        )
        self.mrs_radiobutton().click()
        self.input_value(self.firstname(), firstname)
        self.input_value(self.lastname(), lastname)
        self.input_value(self.passwd(), passwd)
        self.input_value(self.days(), Registration.DATE)
        self.input_value(self.months(), Registration.MONTH)
        self.input_value(self.years(), years)
        self.newsletter_checkbox().click()
        self.optin_checkbox().click()

    def fill_address(self, first_name, last_name, address, city, country, phone):
        """Заполнение секции Your address"""
        logger.info(
            f"Пытаемся заполнить личные данные значениями "
            f"{first_name}{last_name}{address}{city}{country}{phone}"
        )
        self.input_value(self.first_name(), first_name)
        self.input_value(self.last_name(), last_name)
        self.input_value(self.company(), Registration.COMPANY)
        self.input_value(self.address_line1(), address)
        self.input_value(self.address_line2(), Registration.ADDRESS2)
        self.input_value(self.city(), city)
        self.input_value(self.state(), Registration.STATE)
        self.input_value(self.postal_code(), Registration.POSTAL_CODE)
        self.input_value(self.country(), country)
        self.input_value(self.additional_info(), Registration.ADDITIONAL_INFO)
        self.input_value(self.home_phone(), phone)
        self.input_value(self.mobile_phone(), phone)
        self.input_value(self.address_alias(), Registration.ADDRESS_ALIAS)
        self.register_button().click()
