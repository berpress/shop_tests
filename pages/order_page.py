from locators.order_page import OrderPageLocators


class OrderPage:
    def __init__(self, app):
        self.app = app

    def your_shopping_cart_field(self):
        return self.app.driver.find_element(*OrderPageLocators.YOUR_SHOPPING_CART)

    def your_shopping_cart_field_text(self):
        return self.your_shopping_cart_field().text

    def your_shopping_cart(self):
        return self.your_shopping_cart_field_text()
