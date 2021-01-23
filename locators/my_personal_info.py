from selenium.webdriver.common.by import By


class MyPersonalInfoLocators:
    PERSONAL_INFO_BUTTON = (By.XPATH, '//*[@title="Manage my personal information"]')
    FIRSTNAME_BUTTON = (By.XPATH, '//*[@name="firstname"]')
    LASTNAME_BUTTON = (By.XPATH, '//*[@name="lastname"]')
