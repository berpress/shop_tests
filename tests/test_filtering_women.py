from common.constants import Users
import allure


class TestMyOrders:
    @allure.story("Кликаем рандомно на кнопки из фильтра")
    @allure.severity("minor")
    def test_filtering_women(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку Women
        3. Функция рандомно кликает кнопки из фильтра
        """

        app.filtering_women.filter()
        app.login.logout_button_click()
