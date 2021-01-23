from locators.contact_us import ContactUsLocators
from selenium.webdriver.support.ui import Select


class ContactUsPage:
    def __init__(self, app):
        self.app = app

    def contact_us_header_button(self):
        return self.app.driver.find_element(*ContactUsLocators.CONTACT_US_HEADER_BUTTON)

    def contact_us_header_button_click(self):
        """Переход по ссылке"""
        self.contact_us_header_button().click()

    def subject_heading(self):
        return Select(self.app.driver.find_element_by_id('id_contact'))

    def email_address(self):
        return self.app.driver.find_element(*ContactUsLocators.EMAIL_ADDRESS_FIELD)

    def order_reference(self):
        return self.app.driver.find_element(*ContactUsLocators.ORDER_REFERENCE_FIELD)

    def attach_file(self):
        return self.app.driver.find_element(*ContactUsLocators.ATTACH_FILE_FORM)

    def message_field(self):
        return self.app.driver.find_element(*ContactUsLocators.MESSAGE_FIELD)

    def send_button(self):
        return self.app.driver.find_element(*ContactUsLocators.ATTACH_FILE_FORM)

    def send_button_click(self):
        self.send_button().click()

    def fill_contact_us_form(self):
        self.subject_heading().select_by_value('1')
        self.email_address().send_keys("anymail@mail.ru")
        self.order_reference().send_keys("658679")
        self.message_field().send_keys("RandomText")
        self.send_button().click()


