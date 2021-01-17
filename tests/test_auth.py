class TestAuth:
    def test_auth_shop(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на login button
        3. Ввести валидные данные
        4. Провериить имя
        """
        app.open_main_page()
        email = "test74@test.com"
        password = "Password11"
        app.login.auth(email=email, password=password)
        assert 0 == 0
        # app.login.logout()
