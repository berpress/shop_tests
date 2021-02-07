from common.constants import MyAccount
from models.fake_data import PersonalInformationData, Address
import allure


class TestRegistration:
    @allure.story("Открываем страницу и регистрируемся")
    @allure.severity("critical")
    def test_registration(self, app):
        """
        1. Открыть главную страницу
        2. Нажать на кнопку Sign in в хедера
        3. Ввести e-mail
        4. Нажать create an account
        5. Заполнить все поля на форме
        6. Нажать кнопку Register
        """
        user = PersonalInformationData.random()
        email = user.login
        addr = Address.random()
        app.open_main_page()
        app.registration.go_to_registration_form(email)
        app.registration.fill_personal_information(
            user.password, user.firstname, user.lastname, user.years
        )
        app.registration.fill_address(
            user.firstname,
            user.lastname,
            addr.address,
            addr.city,
            addr.country,
            addr.phone,
        )
        assert app.registration.account_header() == MyAccount.MY_ACCOUNT
