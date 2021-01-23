from locators.my_orders import MyOrdersLocators


class MyOrdersPage:
    def __init__(self, app):
        self.app = app

    def my_orders_button(self):
        return self.app.driver.find_element(*MyOrdersLocators.ORDERS_BUTTON)

    def my_orders_button_click(self):
        self.my_orders_button().click()

    def check(self):
        """Функция которая кликает по кнопке 'my_orders info', добавлена для читабельности теста."""
        self.my_orders_button_click()
