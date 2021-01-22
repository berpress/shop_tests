from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.contact_us import ContactUsPage


class Application:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.login = LoginPage(self)
        self.contact_us = ContactUsPage(self)


    def open_main_page(self):
        self.driver.get(self.url)

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()