from common.constants import Users, Registration as reg, RandomData as rand
import allure
import pytest

from models.regdata import RegData


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
        # user = RegData.random()
        # email = user.login
        # addr = Address.random()
        app.open_main_page()
        app.registration.go_to_registration_form(rand.email)
        app.registration.fill_personal_information(
            rand.user.password,
            rand.user.first_name,
            rand.user.last_name,
            rand.date.year,
        )
        app.registration.fill_address(
            rand.user.first_name,
            rand.user.last_name,
            rand.addr.address,
            rand.addr.city,
            rand.addr.country,
            rand.addr.phone,
        )

        assert app.registration.account_header() == "MY ACCOUNT"
        app.login.logout_button_click()

    @pytest.mark.parametrize(
        "email, expected_result",
        [
            pytest.param(
                Users.INVALID_EMAIL_2, reg.EMAIL_ERROR, id="Invalid email address"
            ),
            pytest.param(Users.EMPTY_EMAIL, reg.EMAIL_ERROR, id="Empty email address"),
            pytest.param(Users.EMAIL, reg.EMAIL_EXISTS, id="Existing email"),
        ],
    )
    @allure.story("Регистрация")
    @allure.severity("minor")
    def test_registration_wrong_email(self, app, email, expected_result):
        """
       Негативные тесты для первого шага регистрации,
       где требуется только ввод email
       1. Открыть главную страницу
       2. Нажать на кнопку Sign In в правом верхнем углу
       3. Ввести некорректный e-mail
       4. Ожидается возникновение ошибок
        """
        user = RegData.random()
        app.open_main_page()
        app.registration.go_to_registration_form(email)
        app.registration.fill_personal_information(user)
        error_message = str(app.registration.wrong_email_alert(expected_result))
        assert expected_result in error_message, (
            f"Текст ошибки не соответствует ожидаемому. Текст ошибки:\n "
            f"{error_message}\n, ожидаемый результат:\n {expected_result}"
        )

    # @pytest.mark.parametrize(
    #     "firstname, lastname, address1, city, expected_result",
    #     [
    #         pytest.param(
    #             rand.user.first_name,
    #             "",
    #             rand.addr.address,
    #             rand.addr.city,
    #             reg.LASTNAME_REQUIRED,
    #             id="Empty lastname",
    #         ),
    #         pytest.param(
    #             "",
    #             rand.user.last_name,
    #             rand.addr.address,
    #             rand.addr.city,
    #             reg.FIRSTNAME_REQUIRED,
    #             id="Empty firstname",
    #         ),
    #         pytest.param(
    #             rand.user.first_name,
    #             rand.user.last_name,
    #             "",
    #             rand.addr.city,
    #             reg.ADDRESS_REQUIRED,
    #             id="Empty address",
    #         ),
    #         pytest.param(
    #             rand.user.first_name,
    #             rand.user.last_name,
    #             rand.addr.address,
    #             "",
    #             reg.CITY_REQUIRED,
    #             id="Empty city",
    #         ),
    #     ],
    # )
    # @allure.story("Регистрация")
    # @allure.severity("minor")
    # def test_registration_empty_fields(
    #     self, app, firstname, lastname, address1, city, expected_result
    # ):
    #     """
    #     Негативный тест на возникновение ошибки при незаполненных обязательных полях.
    #     1. Открыть главную страницу
    #     2. Перейти на форму регистрации
    #     3. Заполнить секцию личной информации, игнорируя обязательные поля
    #     4. Заполнить секцию адреса, игнорируя обязательные поля
    #     5. Ожидается возникновение ошибки
    #     """
    #     user = RegData.random()
    #     app.open_main_page()
    #     app.registration.go_to_registration_form(rand.addr.email)
    #     app.registration.fill_personal_information(
    #         user.password, user.firstname, user.lastname, user.years
    #     )
    #     app.registration.fill_address(
    #         user.firstname,
    #         user.lastname,
    #         addr.address,
    #         addr.city,
    #         addr.country,
    #         addr.phone,
    #     )
    #     assert (
    #         app.registration.account_header() == MyAccount.MY_ACCOUNT
    #     ), "Тест упал. Текст ошибки не совпадает с ожидаемым"
