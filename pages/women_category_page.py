from selenium.webdriver import ActionChains
from locators.women_category_page import WomenCategoryLocators


class WomenCategoryPage:
    def __init__(self, app):
        self.app = app

    def women_category_button(self):
        return self.app.driver.find_element(
            *WomenCategoryLocators.WOMEN_CATEGORY_BUTTON
        )

    def women_category_button_click(self):
        self.women_category_button().click()

    def women_category(self):
        self.women_category_button_click()

    def find_good_cart(self):
        return self.app.driver.find_element(*WomenCategoryLocators.GOOD_CART)

    def move_to_good(self):
        good_cart = self.find_good_cart()
        add_to_cart_button = self.add_to_cart_button()
        ActionChains(self.app.driver).move_to_element(good_cart).move_to_element(
            add_to_cart_button
        ).click().perform()

    def add_to_cart_button(self):
        return self.app.driver.find_element(*WomenCategoryLocators.ADD_TO_CART)

    def proceed_to_checkout_button(self):
        return self.app.driver.find_element(*WomenCategoryLocators.PROCEED_TO_CHECKOUT)

    def proceed_to_checkout_button_click(self):
        self.proceed_to_checkout_button().click()

    def proceed_to_checkout(self):
        self.app.driver.implicitly_wait(10)
        self.proceed_to_checkout_button_click()
