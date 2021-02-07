import logging

from locators.my_orders import MyOrdersLocators

logger = logging.getLogger()


class MyOrdersPage:
    def __init__(self, app):
        self.app = app

    def my_orders_button(self):
        return self.app.driver.find_element(*MyOrdersLocators.ORDERS_BUTTON)

    def my_orders_button_click(self):
        logger.info("Открытие страницы с заказами")
        self.my_orders_button().click()

    def header(self):
        return self.app.driver.find_element(*MyOrdersLocators.ORDER_HISTORY)

    def header_text(self):
        return self.header().text
