from selenium.webdriver.common.by import By


class MyAddressesLocators:
    FIRST_AND_SECOND_NAME = (By.CLASS_NAME, 'address_name')
    COMPANY_NAME = (By.CSS_SELECTOR, '.address_company')
    ADDRESS_NAME_1 = (By.CSS_SELECTOR, '.address_address1')
    ADDRESS_NAME_2 = (By.CSS_SELECTOR, '.address_address2')
    CITY_PARTS = (By.CSS_SELECTOR, '.last_item.item.box>li:nth-child(5)>span')
    COUNTRY_NAME = (By.CSS_SELECTOR, '.last_item.item.box > li:nth-child(6)>span')
    PHONE = (By.CSS_SELECTOR, '.address_phone')
    PHONE_MOBILE = (By.CSS_SELECTOR, '.address_phone_mobile')
