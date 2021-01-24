from selenium.webdriver.common.by import By


class ContactUsLocators:
    CONTACT_US_HEADER_BUTTON = (By.ID, "contact-link")

    EMAIL_ADDRESS_FIELD = (By.ID, "email")
    ORDER_REFERENCE_FIELD = (By.ID, "id_order")
    ATTACH_FILE_FORM = (By.ID, "fileUpload")
    MESSAGE_FIELD = (By.ID, "message")
    SEND_BUTTON = (By.ID, "submitMessage")
    SUCCESS_ALERT = (By.XPATH, '//*[@class="alert alert-success"]')
