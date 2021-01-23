class TestMyPersonalInfo:
    def test_my_personal_info(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на My Personal Info
        3. Проверить данные в First Name и Last Name
        """
        app.open_main_page()
        email = "test74@test.com"
        password = "Password11"
        app.login.auth(email=email, password=password)
        app.personal_info.check()
        assert app.personal_info.get_name() == 'Ivan'
        assert app.personal_info.get_lastname() == 'Ivanov'
