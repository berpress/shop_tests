from common.constants import Users, Alerts
import pytest


class TestAuth:
    def test_auth_shop(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на login button
        3. Ввести валидные данные
        4. Проверить имя
        """
        app.open_main_page()
        email = Users.EMAIL
        password = Users.PASSWORD
        app.login.auth(email=email, password=password)
        assert app.login.get_userdata() == Users.ACCOUNT_DATA
        app.login.logout_button_click()

    @pytest.mark.parametrize(
        "email, password, alert",
        (
            (Users.INVALID_EMAIL, Users.INVALID_PASSWORD, Alerts.ALERT_INVALID_DATA),
            (Users.EMPTY_EMAIL, Users.EMPTY_PASSWORD, Alerts.ALERT_EMPTY_DATA),
        ),
    )
    def test_invalid_auth(self, app, email, password, alert):
        """
        1. Открыть страницу
        2. Кликнуть на login button
        3. Ввести невалидные данные
        """
        app.open_main_page()
        app.login.auth(email=email, password=password)
        assert app.login.login_auth_alert_get_text() == alert
