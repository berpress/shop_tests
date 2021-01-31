class TestProceedToCHeckout:
    def test_proceed_to_checkout(self, app, login):
        """
        1. Открыть страницу
        2. Кликнуть категорию покупки ( для примера представлена вумен )
        3. Кликнуть купить платье
        4. Пройти этапы покупки (
        Проверка адреса, выбрать службу доставки , проверка информации о покупки)
        5. Кликнуть способ оплаты банковская карта
        """
        app.women_category_page.women_category()
        app.women_category_page.move_to_good()
        app.women_category_page.proceed_to_checkout()
        app.proceed_to_checkout.buying()
