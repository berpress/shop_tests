from common.constants import Users, Alerts
from models.login import UserData
import pytest
import allure


class TestAuth:
    data = UserData.random()

    @allure.story("Авторизация")
    @allure.severity("blocker")
    def test_auth_shop(self, app, login):
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

    @allure.story("Авторизация")
    @allure.severity("blocker")
    @pytest.mark.parametrize(
        "email, password, alert",
        (
            (data.login, data.password, Alerts.ALERT_INVALID_DATA),
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
