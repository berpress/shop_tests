import logging

from selenium.webdriver.support.select import Select

from common.logger import setup
from locators.proceed_to_checkout import ProceedToCheckoutLocators

logger = logging.getLogger()


class ShoppingCartPage:
    def __init__(self, app):
        setup("INFO")
        logger.setLevel("INFO")
        self.app = app

    def summary_proceed_to_checkout_button(self):
        return self.app.driver.find_element(
            *ProceedToCheckoutLocators.SUMMARY_PROCEED_TO_CHECKOUT
        )

    def summary_proceed_to_checkout_button_click(self):
        self.summary_proceed_to_checkout_button().click()

    def address_pop_up_button(self):
        return self.app.driver.find_element(*ProceedToCheckoutLocators.ADDRESS_SELECT)

    def address_pop_up_button_click(self):
        select = Select(self.address_pop_up_button())
        select.select_by_visible_text("My address")

    def delivery_address(self):
        return self.app.driver.find_elements(
            *ProceedToCheckoutLocators.DELIVERY_ADDRESS_INFO
        )

    def check_address_info(self):
        logger.info("Проверка строк выбранного в попапе адреса при оформлении заказа")
        return [i.text for i in self.delivery_address()]

    def address_proceed_to_checkout_button(self):
        return self.app.driver.find_element(*ProceedToCheckoutLocators.ADDRESS)

    def address_proceed_to_checkout_button_click(self):
        self.address_proceed_to_checkout_button().click()

    def shipping_checkbox(self):
        return self.app.driver.find_element(
            *ProceedToCheckoutLocators.CHECKBOX_SHIPPING
        )

    def shipping_checkbox_click(self):
        self.shipping_checkbox().click()

    def shipping_proceed_to_checkout_button(self):
        return self.app.driver.find_element(*ProceedToCheckoutLocators.SHIPPING)

    def shipping_proceed_to_checkout_button_click(self):
        self.shipping_proceed_to_checkout_button().click()

    def payment_info(self):
        return self.app.driver.find_elements(*ProceedToCheckoutLocators.PAYMENT_INFO)

    def check_payment_info(self):
        logger.info(
            "Проверка информации о выбранном товаре во вкладке "
            "Payment при оформлении заказа"
        )
        return [i.text for i in self.payment_info()]

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
        logger.info("Проверка информации купленного товара")
        data_info = [i.text for i in self.my_store_complete_info()]
        data_info_st = str(data_info[0])
        return data_info_st[0:215]

    def buying_one_step(self):
        self.summary_proceed_to_checkout_button_click()
        self.address_proceed_to_checkout_button_click()
        self.shipping_checkbox_click()
        self.shipping_proceed_to_checkout_button_click()

    def buying_two_step(self):
        self.pay_by_bank_wire_button_click()
        self.confirm_my_order_button_click()

    def select_new_address(self):
        """Функция для теста, где выбирается второй адрес."""
        self.summary_proceed_to_checkout_button_click()
        self.address_pop_up_button_click()

    def confirm_shipping_for_new_address(self):
        """Функция для теста, где выбирается второй адрес."""
        self.address_proceed_to_checkout_button_click()
        self.shipping_checkbox_click()
        self.shipping_proceed_to_checkout_button_click()

    def choose_pay_for_new_address(self):
        """Функция для теста, где выбирается второй адрес."""
        self.pay_by_bank_wire_button_click()
        self.confirm_my_order_button_click()
