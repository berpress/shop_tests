import allure

from common.constants import MyOrdersPage


class TestMyOrders:
    @allure.story("Главная страница-мой аккаунт")
    @allure.severity("minor")
    def test_my_orders(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку My Orders
        """
        app.my_orders.my_orders_button_click()
        assert app.my_orders.header_text() == MyOrdersPage.ORDER_HISTORY
        app.login.logout_button_click()
