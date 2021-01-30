from selenium.webdriver.common.by import By


class WomenCategoryLocators:
    WOMEN_CATEGORY_BUTTON = (By.XPATH, '//*[@class="sf-with-ul" and @title="Women"]')
    GOOD_CART = (
        By.XPATH,
        '//*[@class="replace-2x img-responsive" and @title="Blouse"]',
    )
    ADD_TO_CART = (By.XPATH, '//*[@data-id-product="2"]')
    PROCEED_TO_CHECKOUT = (By.XPATH, '//*[@title="Proceed to checkout"]')
