from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.my_addresses import MyAddressesPage
from pages.contact_us import ContactUsPage
from pages.my_personal_info import MyPersonalInfoPage
from pages.my_orders import MyOrdersPage
from pages.my_credit_slips import MyCreditSlipsPage
from pages.filtering_women import FilteringWomenPage


class Application:
    def __init__(self, url):
        options: Options = Options()
        options.headless = True
        self.url = url
        try:
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options
            )
        except ValueError:
            self.driver = webdriver.Chrome(r"C:\chromedriver.exe", options=options)
        self.login = LoginPage(self)
        self.my_addresses = MyAddressesPage(self)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.login = LoginPage(self)
        self.contact_us = ContactUsPage(self)
        self.personal_info = MyPersonalInfoPage(self)
        self.my_orders = MyOrdersPage(self)
        self.my_credit_slips = MyCreditSlipsPage(self)
        self.filtering_women = FilteringWomenPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()
