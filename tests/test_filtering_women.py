import allure
import pytest


class TestMyOrders:
    @allure.story("Фильтр")
    @allure.severity("minor")
    @pytest.mark.xfail
    def test_filtering_women(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку Women
        3. Функция рандомно кликает кнопки из фильтра

        Тест ожидаемо падает, так как функционал фильтрации пока не реализован,
        поэтому тест промаркирован xfail

        """

        app.filtering_women.filter()
        app.login.logout_button_click()
