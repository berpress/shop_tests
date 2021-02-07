import allure


class TestContactUs:
    @allure.story("Главная страница-информация")
    @allure.severity("minor")
    def test_contact_header(self, app):
        """
        1. Открыть страницу по ссылке из хедера
        2. Заполнить все поля формы
        3. Проверяем успешную отправку сообщения
        """
        app.open_main_page()
        app.contact_us.contact_us_header_button_click()
        app.contact_us.fill_contact_us_form(
            value="1", address="anymail@mail.ru", order="658679", message="RandomText"
        )
        assert (
            app.contact_us.get_text_from_success_alert()
            == "Your message has been successfully sent to our team."
        )
