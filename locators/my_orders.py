from selenium.webdriver.common.by import By


class MyOrdersLocators:
    ORDERS_BUTTON = (By.XPATH, '//*[@title="My orders"]')
    ORDER_HISTORY = (By.XPATH, '//*[@class="page-heading bottom-indent"]')
