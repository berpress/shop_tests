class TestMyPersonalInfo:
    def test_my_personal_info(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть на My Personal Info
        3. Проверить данные в First Name и Last Name
        """

        app.personal_info.check()
        assert app.personal_info.get_name() == 'Ivan'
        assert app.personal_info.get_lastname() == 'Ivanov'
        app.login.logout_button_click()
