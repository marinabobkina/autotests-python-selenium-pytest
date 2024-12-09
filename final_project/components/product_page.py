import allure
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from final_project.helpers.functions import *


class ProductPage(Base):

    PAGE_TITLE = ("xpath", "// h1[contains(text(), 'Пицца «Как у бабушки»')]")
    PIZZA_NAME = ("xpath", "//h1[@class='product_title entry-title']")
    PIZZA_PRICE = ("xpath", "(//span/bdi)[1]")
    OPTION_FIELD = ("xpath", "//select[@id='board_pack']")
    OPTION_VARIANT = ("xpath", "//select/option[contains(text(), 'Сырный')]")
    BUTTON_TO_CART = ("xpath", "//button[@name='add-to-cart']")

    def is_product_page(self):
        with allure.step(
            "Проверить, что отображается страница с информацией о выбранной в слайдере пицце."
        ):
            product_title = self.wait.until(
                EC.visibility_of_element_located(self.PAGE_TITLE)
            )
            assert product_title.text == "Пицца «Как у бабушки»"

    def option_field_click(self):
        with allure.step("Кликнуть в поле выбора борта пиццы."):
            self.wait.until(EC.element_to_be_clickable(self.OPTION_FIELD)).click()

    def find_option_variant(self):
        with allure.step("Найти выпадающее окно со списком вариантов борта."):
            option = self.wait.until(EC.element_to_be_clickable(self.OPTION_VARIANT))
            return option

    def choose_option_variant(self):
        with allure.step("Выбрать один из вариантов борта."):
            self.find_option_variant().click()

    def option_price(self):
        with allure.step("Найти стоимость выбранного борта пиццы."):
            option_price = self.find_option_variant().get_attribute("value")
            option_price_int = extract_figures(option_price)
            return option_price_int

    def pizza_price(self):
        with allure.step("Найти стоимость пиццы на странице с описанием продукта."):
            pizza_price = self.wait.until(
                EC.visibility_of_element_located(self.PIZZA_PRICE)
            ).text
            pizza_price_int = extract_figures(pizza_price)
            return pizza_price_int

    def pizza_name(self):
        with allure.step("Найти название пиццы на странице с описанием продукта."):
            pizza_name = self.wait.until(
                EC.visibility_of_element_located(self.PIZZA_NAME)
            ).text.upper()
            return pizza_name

    def click_button_to_cart(self):
        with allure.step("Нажать кнопку 'В корзину' на странице с описанием продукта."):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_TO_CART)).click()
