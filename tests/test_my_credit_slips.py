import allure
from common.constants import MyCreditSlips


class TestMyCreditSlips:
    @allure.story("Главная страница-мой аккаунт")
    @allure.severity("minor")
    def test_my_orders(self, app, login):
        """
        1. Открыть главную страницу
        2. Кликнуть на ссылку My Credit Slips в футере страницы
        3. Открывается страница с привязанными картами
        4. Нажать на кнопку выхода в правом вернем углу
        5. Происходит разлогин
        """
        app.my_credit_slips.check()
        assert app.my_credit_slips.my_c_s_field_text() == MyCreditSlips.MY_CREDIT_SLIPS
