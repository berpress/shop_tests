from locators.main_page import SearchLocators


class SearchGoods:
    def __init__(self, app):
        self.app = app

    def search_field(self):
        return self.app.driver.find_element(*SearchLocators.SEARCH_FIELD)

    def search_button(self):
        return self.app.driver.find_element(*SearchLocators.SEARCH_BUTTON)

    def run_search(self, str):
        self.search_field().send_keys(str)
        self.search_button().click()

    def negative_alert(self):
        return self.app.driver.find_element(*SearchLocators.NOT_FOUND_ALERT).text

    def found_items(self):
        return self.app.driver.find_elements(*SearchLocators.FOUND_ITEMS)

    def check_found_item(self, str):
        """Проверка заголовков найденных элементов на вхождение строки"""
        list = self.found_items()
        for i in list:
            if i.text.lower().find(str.lower()) != -1:
                return True
        return False