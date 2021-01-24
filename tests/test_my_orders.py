class TestMyOrders:
    def test_my_orders(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку My Orders
        """

        app.my_orders.check()
        app.login.logout_button_click()
