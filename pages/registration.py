from common.constants import Registration
from locators.registration import RegistrationLocators
from models.exception import NoneTypeError
import logging


logger = logging.getLogger()


class RegistrationPage:
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
        self.app.implicitly_wait()
        return self.app.driver.find_element(*RegistrationLocators.ACCOUNT_HEADER).text

    def go_to_registration_form(self, email):
        self.sign_in_header_button().click()
        self.email_field().send_keys(email)
        self.create_account_button().click()

    def fill_personal_information(self, passwd, firstname, lastname, years):
        """Заполнение секции Your personal information"""
        self.app.implicitly_wait()
        logger.info("Выбор пола")
        self.mrs_radiobutton().click()
        logger.info("Заполнение поля firstname")
        self.firstname().send_keys(self.check_param(firstname))
        logger.info("Заполнение поля lastname")
        self.lastname().send_keys(self.check_param(lastname))
        logger.info("Заполнение поля password")
        self.passwd().send_keys(self.check_param(passwd))
        logger.info("Заполнение поля date")
        self.days().send_keys(Registration.DATE)
        logger.info("Заполнение поля month")
        self.months().send_keys(Registration.MONTH)
        logger.info("Заполнение поля years")
        self.years().send_keys(years)
        logger.info("Выбор чекбокса newsletter")
        self.newsletter_checkbox().click()
        logger.info("Выбор чекбокса special_offers")
        self.optin_checkbox().click()

    def check_param(self, param):
        if param is not None:
            return param
        else:
            raise NoneTypeError

    def fill_address(self, first_name, last_name, address, city, country, phone):
        """Заполнение секции Your address"""
        logger.info("Заполнение поля first_name")
        self.first_name().send_keys(self.check_param(first_name))
        logger.info("Заполнение поля last_name")
        self.last_name().send_keys(self.check_param(last_name))
        logger.info("Заполнение поля company")
        self.company().send_keys(self.check_param(Registration.COMPANY))
        logger.info("Заполнение поля address_line1")
        self.address_line1().send_keys(self.check_param(address))
        logger.info("Заполнение поля address_line2")
        self.address_line2().send_keys(self.check_param(Registration.ADDRESS2))
        logger.info("Заполнение поля city")
        self.city().send_keys(self.check_param(city))
        logger.info("Заполнение поля state")
        self.state().send_keys(self.check_param(Registration.STATE))
        logger.info("Заполнение поля postal_code")
        self.postal_code().send_keys(self.check_param(Registration.POSTAL_CODE))
        logger.info("Заполнение поля country")
        self.country().send_keys(self.check_param(country))
        logger.info("Заполнение поля additional_info")
        self.additional_info().send_keys(self.check_param(Registration.ADDITIONAL_INFO))
        logger.info("Заполнение поля home_phone")
        self.home_phone().send_keys(self.check_param(phone))
        logger.info("Заполнение поля mobile_phone")
        self.mobile_phone().send_keys(self.check_param(phone))
        logger.info("Заполнение поля address_alias")
        self.address_alias().send_keys(self.check_param(Registration.ADDRESS_ALIAS))
        logger.info("Клик на кнопку Register")
        self.register_button().click()
