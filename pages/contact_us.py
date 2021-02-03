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
        return Select(self.app.driver.find_element_by_id("id_contact"))

    def email_address(self):
        return self.app.driver.find_element(*ContactUsLocators.EMAIL_ADDRESS_FIELD)

    def order_reference(self):
        return self.app.driver.find_element(*ContactUsLocators.ORDER_REFERENCE_FIELD)

    def attach_file(self):
        return self.app.driver.find_element(*ContactUsLocators.ATTACH_FILE_FORM)

    def message_field(self):
        return self.app.driver.find_element(*ContactUsLocators.MESSAGE_FIELD)

    def send_button(self):
        return self.app.driver.find_element(*ContactUsLocators.SEND_BUTTON)

    def send_button_click(self):
        self.send_button().click()

    def get_text_from_success_alert(self) -> str:
        return self.success_alert().text

    def success_alert(self) -> str:
        return self.app.driver.find_element(*ContactUsLocators.SUCCESS_ALERT)

    def check_success_alert(self) -> bool:
        return self.app.driver.find_element(
            *ContactUsLocators.SUCCESS_ALERT
        ).is_displayed()

    def fill_contact_us_form(self, value, address, order, message):
        self.app.driver.implicitly_wait(10)
        self.subject_heading().select_by_value(value)
        self.email_address().send_keys(address)
        self.order_reference().send_keys(order)
        self.message_field().send_keys(message)
        self.send_button_click()
