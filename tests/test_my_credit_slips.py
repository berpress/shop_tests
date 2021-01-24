from common.constants import Users


class TestMyOrders:
    def test_my_orders(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку My Credit Slips
        """
        app.my_credit_slips.check()
        app.login.logout_button_click()
