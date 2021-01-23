from common.constants import *


class TestAuth:
    def test_auth_shop(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на login button
        3. Ввести валидные данные
        4. Проверить имя
        """
        app.open_main_page()
        email = EMAIL
        password = PASSWORD
        app.login.auth(email=email, password=password)
        assert app.login.get_userdata() == ACCOUNT_DATA
        app.login.logout_button_click()

    def test_auth_shop_invalid_password(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на login button
        3. Ввести валидный email и невалидный password
        4. Проверить текст alert'a
        """
        app.open_main_page()
        email = EMAIL
        password = INVALID_PASSWORD
        app.login.auth(email=email, password=password)
        assert app.login.login_auth_alert_get_text() == ALERT_INVALID_DATA

    def test_auth_shop_empty_data(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на login button
        3. Оставить поля email и password пустыми
        4. Проверить текст alert'a
        """
        app.open_main_page()
        email = EMPTY_EMAIL
        password = EMPTY_PASSWORD
        app.login.auth(email=email, password=password)
        assert app.login.login_auth_alert_get_text() == ALERT_EMPTY_DATA
