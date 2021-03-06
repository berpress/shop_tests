from common.my_addresses_values import MyAddressesValues
import allure


class TestMyAddresses:
    @allure.story("Главная страница-мой аккаунт")
    @allure.severity("minor")
    def test_my_addresses(self, app, login):
        """
        1. Авторизоваться
        2. Выбрать раздел My addresses в футере
        3. Проверить, что информация соотвествует данным пользователя при регистрации
        """
        app.my_addresses.open_my_addresses()
        assert (
            app.my_addresses.get_first_and_second_name()[0]
            == MyAddressesValues.first_name
        )
        assert (
            app.my_addresses.get_first_and_second_name()[1]
            == MyAddressesValues.second_name
        )
        assert app.my_addresses.get_company_name() == MyAddressesValues.company_name
        assert app.my_addresses.get_address_name1() == MyAddressesValues.address_name_1
        assert app.my_addresses.get_address_name2() == MyAddressesValues.address_name_2
        assert app.my_addresses.get_city_parts()[0] == MyAddressesValues.city_part1
        assert app.my_addresses.get_city_parts()[1] == MyAddressesValues.city_part2
        assert app.my_addresses.get_city_parts()[2] == MyAddressesValues.city_part3
        assert app.my_addresses.get_country_name() == MyAddressesValues.country_name
        assert app.my_addresses.get_phone() == MyAddressesValues.phone
        assert app.my_addresses.get_phone_mobile() == MyAddressesValues.phone_mobile
