from selenium.webdriver.common.by import By


class MyAddressesLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '.address_name:nth-child(1)')
    SECOND_NAME = (By.CSS_SELECTOR, '.address_name:nth-child(2)')
    COMPANY_NAME = (By.CSS_SELECTOR, '.address_company')
    ADDRESS_NAME_1 = (By.CSS_SELECTOR, '.address_address1')
    ADDRESS_NAME_2 = (By.CSS_SELECTOR, '.address_address2')
    CITY_PART1 = (By.CSS_SELECTOR, '.last_item.item.box>li:nth-child(5)>span:nth-child(1)')
    CITY_PART2 = (By.CSS_SELECTOR, '.last_item.item.box>li:nth-child(5)>span:nth-child(2)')
    CITY_PART3 = (By.CSS_SELECTOR, '.last_item.item.box>li:nth-child(5)>span:nth-child(3)')
    COUNTRY_NAME = (By.CSS_SELECTOR, '.last_item.item.box > li: nth - child(6) > span')
    PHONE = (By.CSS_SELECTOR, '.address_phone')
    PHONE_MOBILE = (By.CSS_SELECTOR, '.address_phone_mobile')
