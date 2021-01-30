class TestMyOrders:
    def test_filtering_women(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть на кнопку Women
        3. Функция рандомно кликает кнопки из фильтра
        """

        app.filtering_women.filter()
        app.login.logout_button_click()
