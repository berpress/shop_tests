class TestContactUs:
    def test_contact_header(self, app):
        """
        1. Открыть страницу по ссылке из хедера
        """
        app.open_main_page()
        app.contact_us.contact_us_header_button_click()
        app.contact_us.fill_contact_us_form()


        assert 0 == 0


