from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.my_addresses import MyAddressesPage


class Application:
    def __init__(self, url):
        self.url = url
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        except ValueError:
            self.driver = webdriver.Chrome('C:\chromedriver.exe')
        self.login = LoginPage(self)
        self.my_addresses = MyAddressesPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()
