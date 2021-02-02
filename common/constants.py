class Users:
    ACCOUNT_DATA = "Ivan Ivanov"
    EMAIL = "admin2@admin.ru"
    PASSWORD = "Password11"
    INVALID_EMAIL = "test44@testcom"
    INVALID_PASSWORD = "Password22"
    EMPTY_EMAIL = ""
    EMPTY_PASSWORD = ""


class Alerts:
    ALERT_INVALID_DATA = "There is 1 error\nAuthentication failed."
    ALERT_EMPTY_DATA = "There is 1 error\nAn email address required."


class Cart:
    YOUR_SHOPPING_CART = "Your shopping cart"


class SearchStrings:
    """Строки для параметризации теста поиска по каталогу"""

    PART_OF_WORD = "dre"
    ONE_WORD = "dress"
    TWO_WORDS = "Printed Summer"
    ONE_WORD_NEGATIVE = "siurhfsuew"
    TWO_WORDS_NEGATIVE = "siurh fsuew"

class MyCreditSlips:
    MY_CREDIT_SLIPS = "CREDIT SLIPS"


class MyOrdersPage:
    ORDER_HISTORY = "ORDER HISTORY"


class Registration:
    EMAIL_ERROR = "Invalid email address"
    EMAIL_EXISTS = "has already been registered"
    LASTNAME_REQUIRED = "lastname is required"
    FIRSTNAME_REQUIRED = "firstname is required"
    ADDRESS_REQUIRED =  "is required"
    CITY_REQUIRED = "city is required"
