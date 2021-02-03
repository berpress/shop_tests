import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from common.logger import setup
from pages.contact_us import ContactUsPage
from pages.login import LoginPage
from pages.my_addresses import MyAddressesPage
from pages.my_credit_slips import MyCreditSlipsPage
from pages.my_orders import MyOrdersPage
from pages.my_personal_info import MyPersonalInfoPage
from pages.main_page import SearchGoods


from pages.women_category_page import WomenCategoryPage
from pages.order_page import OrderPage
from pages.registration import RegistrationPage
from pages.filtering_women import FilteringWomenPage

from pages.order_page import OrderPage
from pages.registration import RegistrationPage
from pages.filtering_women import FilteringWomenPage
from pages.women_category_page import WomenCategoryPage

logger = logging.getLogger()


class Application:
    def __init__(self, headless, url):
        setup("INFO")
        logger.setLevel("INFO")
        options: Options = Options()
        if headless:
            options.add_argument("--headless")
        self.url = url
        try:
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options
            )
        except ValueError:
            self.driver = webdriver.Chrome(r"C:\chromedriver.exe", options=options)
        self.login = LoginPage(self)
        self.my_addresses = MyAddressesPage(self)
        self.contact_us = ContactUsPage(self)
        self.personal_info = MyPersonalInfoPage(self)
        self.my_orders = MyOrdersPage(self)
        self.my_credit_slips = MyCreditSlipsPage(self)
        self.women_category_page = WomenCategoryPage(self)
        self.order_page = OrderPage(self)
        self.registration = RegistrationPage(self)
        self.filtering_women = FilteringWomenPage(self)
        self.search = SearchGoods(self)

    def open_main_page(self):
        logger.info("Open main page")
        self.driver.get(self.url)

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()
