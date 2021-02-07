import allure
import pytest


class TestMyOrders:
    @allure.story("Фильтр")
    @allure.severity("minor")
    @pytest.mark.xfail(reason="Функционал пока не реализован")
    def test_filtering_women(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку Women
        3. Функция рандомно кликает кнопки из фильтра

        """

        app.filtering_women.filter()
        app.login.logout_button_click()
