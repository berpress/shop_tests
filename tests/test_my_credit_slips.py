from common.constants import Users


class TestMyOrders:
    def test_my_orders(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку My Credit Slips
        """
        app.open_main_page()
        email = Users.EMAIL
        password = Users.PASSWORD
        app.login.auth(email=email, password=password)
        app.my_credit_slips.check()
        app.login.logout_button_click()
