from models.fake_data import UserData, Address, Date
from common.constants import Users, Registration as reg
import allure
import pytest

user = UserData.random()
email = user.login
date = Date.random()
addr = Address.random()

class TestRegistration:
    @allure.story("Регистрация")
    @allure.severity("critical")
    def test_registration(self, app):
        """
        Позитивный тест
        1. Открыть главную страницу
        2. Нажать на кнопку Sign in в хедере
        3. Ввести e-mail
        4. Нажать create an account
        5. Заполнить все поля на форме
        6. Нажать кнопку Register
        """
        app.open_main_page()
        app.registration.go_to_registration_form(email)
        app.registration.fill_personal_information(
            user.password, user.first_name, user.last_name, date.year
        )
        app.registration.fill_address(
            user.first_name,
            user.last_name,
            addr.address,
            addr.city,
            addr.country,
            addr.phone,
        )
        assert app.registration.account_header() == "MY ACCOUNT"


    @pytest.mark.parametrize(
        "email, expected_result",
        [
            pytest.param(Users.INVALID_EMAIL_2, reg.EMAIL_ERROR, id='1."Invalid email address"'),
            pytest.param(Users.EMPTY_EMAIL, reg.EMAIL_ERROR, id='2."Empty email address'),
            pytest.param(Users.EMAIL, reg.EMAIL_EXISTS, id='3."Existing email"'),
        ],
    )
    @allure.story("Регистрация")
    @allure.severity("critical")
    def test_registration_wrong_email(self, app, email, expected_result):
        """
       Негативные тесты для первого шага регистрации,
       где требуется только ввод email
        """
        app.open_main_page()
        app.registration.go_to_registration_form(email)
        alert = app.registration.wrong_email_alert()

        assert expected_result in alert

    @pytest.mark.parametrize(
        "firstname, lastname, address1, city, expected_result",
        [
            pytest.param(user.first_name, '',  addr.address, addr.city, reg.LASTNAME_REQUIRED, id='1."Empty lastname"'),
            pytest.param('', user.last_name,  addr.address, addr.city, reg.FIRSTNAME_REQUIRED, id='2."Empty firstname'),
            pytest.param(user.first_name, user.last_name, '', addr.city, reg.ADDRESS_REQUIRED, id='3."Empty address"'),
            pytest.param(user.first_name, user.last_name,  addr.address, '', reg.CITY_REQUIRED, id='3."Empty city"')
        ],
    )
    @allure.story("Регистрация")
    @allure.severity("critical")
    def test_registration(self, app, firstname, lastname, address1, city, expected_result):
        """
        Негативный тест на возникновение ошибки при незаполненных обязательных полях.
        """
        app.open_main_page()
        app.registration.go_to_registration_form(email)
        app.registration.fill_personal_information(
            user.password, firstname, lastname, date.year
        )
        app.registration.fill_address(
            user.first_name,
            user.last_name,
            address1,
            city,
            addr.country,
            addr.phone,
        )
        error_text = app.registration.errors()
        assert expected_result in error_text
