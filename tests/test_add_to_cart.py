from common.constants import Cart


class TestAddToCart:
    def test_add_to_cart(self, app, login):
        """
        1. Выбрать раздел Women
        2. Переместить мышь на карточку товара
        3. Кликнуть на кнопку "Добавить в корзину"
        4. Перейти к оформлению заказа
        """
        app.open_main_page()
        app.women_category_page.women_category()
        app.women_category_page.move_to_good()
        app.women_category_page.proceed_to_checkout()
        assert app.order_page.your_shopping_cart() == Cart.YOUR_SHOPPING_CART
