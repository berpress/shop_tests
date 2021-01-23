from typing import Any

from locators.main_page import MainLocators
from locators.my_addresses import MyAddressesLocators


class MyAddressesPage:
    def __init__(self, app):
        self.app = app

    def my_addresses_button(self):
        return self.app.driver.find_element(*MainLocators.MY_ADDRESSES)

    def open_my_addresses(self):
        self.my_addresses_button().click()

    def get_first_and_second_name(self) -> Any:
        person_data = self.app.driver.find_elements(*MyAddressesLocators.FIRST_AND_SECOND_NAME)
        return [value.text for value in person_data]

    def get_company_name(self) -> str:
        return self.app.driver.find_element(*MyAddressesLocators.COMPANY_NAME).text

    def get_address_name1(self) -> str:
        return self.app.driver.find_element(*MyAddressesLocators.ADDRESS_NAME_1).text

    def get_address_name2(self) -> str:
        return self.app.driver.find_element(*MyAddressesLocators.ADDRESS_NAME_2).text

    def get_city_parts(self) -> list:
        person_city_data = self.app.driver.find_elements(*MyAddressesLocators.CITY_PARTS)
        return [value.text for value in person_city_data]

    def get_country_name(self) -> str:
        return self.app.driver.find_element(*MyAddressesLocators.COUNTRY_NAME).text

    def get_phone(self) -> str:
        return self.app.driver.find_element(*MyAddressesLocators.PHONE).text

    def get_phone_mobile(self) -> str:
        return self.app.driver.find_element(*MyAddressesLocators.PHONE_MOBILE).text

    # def check_all_lines(self):
    #     if (self.get_first_and_second_name()[0] == MyAddressesValues.first_name
    #             and self.get_first_and_second_name()[1] == MyAddressesValues.second_name
    #             and self.get_company_name() == MyAddressesValues.company_name
    #             and self.get_address_name1() == MyAddressesValues.address_name_1
    #             and self.get_address_name2() == MyAddressesValues.address_name_2
    #             and self.get_city_part1() == MyAddressesValues.city_part1
    #             and self.get_city_part2() == MyAddressesValues.city_part2
    #             and self.get_city_part3() == MyAddressesValues.city_part3
    #             and self.get_country_name() == MyAddressesValues.country_name
    #             and self.get_phone() == MyAddressesValues.phone_mobile):
    #         return True
    #     else:
    #         return False
    #
    # def check_my_addresses(self):
    #     self.my_addresses_button_click()
    #     self.check_all_lines()
