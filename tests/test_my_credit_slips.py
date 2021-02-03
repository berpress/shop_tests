import allure
from common.constants import MyCreditSlips


class TestMyCreditSlips:
    @allure.story("Главная страница-мой аккаунт")
    @allure.severity("minor")
    def test_my_orders(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку My Credit Slips
        """
        app.my_credit_slips.check()
        assert app.my_credit_slips.my_c_s_field_text() == MyCreditSlips.MY_CREDIT_SLIPS
        app.login.logout_button_click()
