from selenium.webdriver.common.by import By


class RegistrationLocators:

    SIGN_IN_BUTTON = (By.CLASS_NAME, "login")
    EMAIL_FIELD = (By.ID, "email_create")
    CREATE_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    HEADING = (By.CLASS_NAME, "page-subheading")
    MR_RADIOBUTTON = (By.ID, "uniform-id_gender1")
    MS_RADIOBUTTON = (By.ID, "uniform-id_gender2")

    FIRSTNAME = (By.ID, "customer_firstname")
    LASTNAME = (By.ID, "customer_lastname")
    EMAIL = (By.ID, "email")
    PASSWD = (By.ID, "passwd")

    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")

    NEWSLETTER_CHECKBOX = (By.ID, "uniform - newsletter")
    OPTIN_CHECKBOX = (By.ID, "uniform - optin")

    # SUCCESS_ALERT = (By.XPATH, '//*[@class="alert alert-success"]')
