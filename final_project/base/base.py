import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    MAIN_PAGE = ("xpath", "//a[@aria-current='page']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open_page(self):
        with allure.step("Открыть сайт: https://pizzeria.skillbox.cc/"):
            self.driver.get("https://pizzeria.skillbox.cc/")

    def is_main_page(self):
        with allure.step("Проверить, что открыт сайт: https://pizzeria.skillbox.cc/."):
            page_name = self.wait.until(EC.url_to_be("https://pizzeria.skillbox.cc/"))
            assert (
                page_name is True
            ), "Ошибка: url не соответствует https://pizzeria.skillbox.cc/."
