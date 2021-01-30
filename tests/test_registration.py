from models.fake_data import UserData, Address, Date


class TestRegistration:
    def test_registration(self, app):
        """
        1. Открыть главную страницу
        2. Нажать на кнопку Sign in в хедера
        3. Ввести e-mail
        4. Нажать create an account
        5. Заполнить все поля на форме
        6. Нажать кнопку Register
        """
        user = UserData.random()
        email = user.login
        date = Date.random()
        addr = Address.random()
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
