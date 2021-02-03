from selenium.webdriver.common.by import By


class MyCreditSlipsLocators:
    CREDIT_SLIPS_BUTTON = (By.XPATH, '//*[@title="My credit slips"]')
    CREDIT_SLIPS_TEXT = (By.XPATH, '//*[@class="page-heading bottom-indent"]')
