from common.shop_value import ShopValues


class TestProceedToCHeckout:
    def test_proceed_to_checkout(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть категорию покупки ( для примера представлена вумен )
        3. Кликнуть купить платье
        4. Пройти этапы покупки (
        адрес, служба доставки , проверка информации о покупке)
        5. Кликнуть способ оплаты банковская карта
        """
        app.women_category_page.women_category()
        app.women_category_page.move_to_good()
        app.women_category_page.proceed_to_checkout()
        app.shopping_cart.buying_one_step()
        assert app.shopping_cart.check_payment_info() == ShopValues.VALUE_GOOD
        app.shopping_cart.buying_two_step()
        assert (
            app.shopping_cart.check_my_store_complete_info()[0]
            == ShopValues.COMPLETE_INFO[0]
        )

    def test_proceed_to_checkout_with_new_address(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть категорию покупки ( для примера представлена вумен )
        3. Кликнуть купить платье
        4. На этапе покупки "выбрать адрес" кликнуть в поп-апе новый адрес
        4. Пройти этапы покупки (
         выбрать службу доставки , проверка информации о покупки)
        5. Кликнуть способ оплаты банковская карта
        """
        app.women_category_page.women_category()
        app.women_category_page.move_to_good()
        app.women_category_page.proceed_to_checkout()
        app.shopping_cart.buying_with_new_address_one_step()
        assert app.shopping_cart.check_address_info() == ShopValues.DELIVERY_INFO
        app.shopping_cart.buying_with_new_address_two_step()
        assert app.shopping_cart.check_payment_info() == ShopValues.VALUE_GOOD
        app.shopping_cart.buying_with_new_address_three_step()
        assert (
            app.shopping_cart.check_my_store_complete_info()[0]
            == ShopValues.COMPLETE_INFO[0]
        )
