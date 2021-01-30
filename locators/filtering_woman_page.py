from selenium.webdriver.common.by import By


class FilterWomanLocators:
    WOMEN_BUTTON = (By.XPATH, '//*[@title="Women"]')
    FILTERING_BUTTONS = (By.XPATH, '//li[@class="nomargin hiddable col-lg-6"]')
