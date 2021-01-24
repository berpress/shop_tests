from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.my_personal_info import MyPersonalInfoPage


class Application:
    def __init__(self, url):
        options: Options = Options()
        options.headless = True
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.login = LoginPage(self)
        self.personal_info = MyPersonalInfoPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()


