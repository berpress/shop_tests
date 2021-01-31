from selenium.webdriver.common.by import By


class MainLocators:
    MY_ADDRESSES = (By.CSS_SELECTOR, '[title="My addresses"]')


class SearchLocators:
    SEARCH_FIELD = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")
    NOT_FOUND_ALERT = (By.ID, "center_column")
    FOUND_ITEMS = (By.CLASS_NAME, "product-name")
