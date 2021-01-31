import allure

class TestMyOrders:
    @allure.story("Открываем страницу и кликаем на My Credit Slips")
    @allure.severity("minor")
    def test_my_orders(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку My Credit Slips
        """
        app.my_credit_slips.check()
        app.login.logout_button_click()
