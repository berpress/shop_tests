import allure
import pytest

from models.contact_us import ContactUsData


class TestContactUs:
    data = ContactUsData.random()

    @allure.story("Главная страница-информация")
    @allure.severity("minor")
    @pytest.mark.parametrize(
        "value, address, order, message",
        ([(data.value, data.address, data.order, data.message)]),
    )
    def test_contact_header(self, app, value, address, order, message):
        """
        1. Открыть страницу по ссылке из хедера
        2. Заполнить все поля формы
        3. Проверяем успешную отправку сообщения
        """
        app.open_main_page()
        app.contact_us.contact_us_header_button_click()
        app.contact_us.fill_contact_us_form(
            value=value, address=address, order=order, message=message
        )
        assert (
            app.contact_us.get_text_from_success_alert()
            == "Your message has been successfully sent to our team."
        )
