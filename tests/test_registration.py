from models.fake_data import RegData, Address
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
        user = RegData.random()
        email = user.login
        addr = Address.random()
        app.open_main_page()
        app.registration.go_to_registration_form(email)
        app.registration.fill_personal_information(user)
        app.registration.fill_address(
            user.firstname,
            user.lastname,
            addr.address,
            addr.city,
            addr.country,
            addr.phone,
        )
        assert app.registration.account_header() == "MY ACCOUNT"
