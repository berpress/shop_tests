class TestMyAddresses:
    def test_my_addresses(self, app):
        app.open_main_page()
        email = "test74@test.com"
        password = "Password11"
        app.login.auth(email=email, password=password)
        assert 0 == 0
        app.my_addresses.check_my_addresses()
        assert 0 == 0

