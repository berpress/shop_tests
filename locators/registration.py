from selenium.webdriver.common.by import By


class RegistrationLocators:

    SIGN_IN_BUTTON = (By.CLASS_NAME, "login")
    EMAIL_CREATE = (By.ID, "email_create")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    HEADING = (By.CLASS_NAME, "page-subheading")
    MR_RADIOBUTTON = (By.ID, "id_gender1")
    MRS_RADIOBUTTON = (By.ID, "id_gender2")

    FIRSTNAME = (By.ID, "customer_firstname")
    LASTNAME = (By.ID, "customer_lastname")
    EMAIL = (By.ID, "email")
    PASSWD = (By.ID, "passwd")

    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")

    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OPTIN_CHECKBOX = (By.ID, "optin")

    # Your address section

    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    COMPANY = (By.ID, "company")
    ADDRESS_LINE1 = (By.ID, "address1")
    ADDRESS_LINE2 = (By.ID, "address2")
    CITY = (By.ID, "city")
    STATE = (By.ID, "id_state")
    POSTAL_CODE = (By.ID, "postcode")
    COUNTRY = (By.ID, "id_country")
    ADDITIONAL_INFO = (By.ID, "other")
    HOME_PHONE = (By.ID, "phone")
    MOBILE_PHONE = (By.ID, "phone_mobile")
    ADDRESS_ALIAS = (By.ID, "alias")
    REGISTER_BUTTON = (By.ID, "submitAccount")

    ACCOUNT_HEADER = (By.XPATH, '//*[@class="page-heading"]')
