from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage
from pages.my_personal_info import MyPersonalInfoPage


class Application:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.login = LoginPage(self)
        self.personal_info = MyPersonalInfoPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def waiting(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()


