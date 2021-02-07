from locators.order_page import OrderPageLocators


class OrderPage:
    def __init__(self, app):
        self.app = app

    def shop_cart_field(self):
        return self.app.driver.find_element(*OrderPageLocators.YOUR_SHOPPING_CART)

    def shop_cart_field_text(self):
        return self.shop_cart_field().text

    def shop_cart(self):
        return self.shop_cart_field_text()
