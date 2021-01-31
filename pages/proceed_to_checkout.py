from locators.proceed_to_checkout import ProceedToCheckoutLocators
from models.iter_info import IterData


class ProceedToCheckoutPage:
    def __init__(self, app):
        self.app = app

    def summary_proceed_to_checkout_button(self):
        return self.app.driver.find_element(
            *ProceedToCheckoutLocators.SUMMARY_PROCEED_TO_CHECKOUT
        )

    def summary_proceed_to_checkout_button_click(self):
        self.summary_proceed_to_checkout_button().click()

    def delivery_address(self):
        return self.app.driver.find_elements(
            *ProceedToCheckoutLocators.DELIVERY_ADDRESS_INFO
        )

    def billing_address(self):
        return self.app.driver.find_elements(
            *ProceedToCheckoutLocators.BILLING_ADDRESS_INFO
        )

    def check_delivery_address(self):
        IterData.check_data(self.delivery_address())

    def check_billing_address(self):
        IterData.check_data(self.billing_address())

    def address_proceed_to_checkout_button(self):
        return self.app.driver.find_element(
            *ProceedToCheckoutLocators.ADDRESS_PROCEED_TO_CHECKOUT
        )

    def address_proceed_to_checkout_button_click(self):
        self.address_proceed_to_checkout_button().click()

    def shipping_checkbox(self):
        return self.app.driver.find_element(
            *ProceedToCheckoutLocators.CHECKBOX_SHIPPING
        )

    def shipping_checkbox_click(self):
        self.shipping_checkbox().click()

    def shipping_proceed_to_checkout_button(self):
        return self.app.driver.find_element(
            *ProceedToCheckoutLocators.SHIPPING_PROCEED_TO_CHECKOUT
        )

    def shipping_proceed_to_checkout_button_click(self):
        self.shipping_proceed_to_checkout_button().click()

    def payment_info(self):
        return self.app.driver.find_elements(*ProceedToCheckoutLocators.PAYMENT_INFO)

    def check_payment_info(self):
        IterData.check_data(self.payment_info())

    def pay_by_bank_wire_button(self):
        return self.app.driver.find_element(*ProceedToCheckoutLocators.PAY_BY_BANK_WIRE)

    def pay_by_bank_wire_button_click(self):
        self.pay_by_bank_wire_button().click()

    def confirm_my_order_button(self):
        return self.app.driver.find_element(*ProceedToCheckoutLocators.CONFIRM_MY_ORDER)

    def confirm_my_order_button_click(self):
        self.confirm_my_order_button().click()

    def my_store_complete_info(self):
        return self.app.driver.find_elements(
            *ProceedToCheckoutLocators.MY_STORE_COMPLETE
        )

    def check_my_store_complete_info(self):
        IterData.check_data(self.my_store_complete_info())

    def buying(self):
        self.summary_proceed_to_checkout_button_click()
        self.check_delivery_address()
        self.check_billing_address()
        self.address_proceed_to_checkout_button_click()
        self.shipping_checkbox_click()
        self.shipping_proceed_to_checkout_button_click()
        self.check_payment_info()
        self.pay_by_bank_wire_button_click()
        self.confirm_my_order_button_click()
        self.check_my_store_complete_info()
