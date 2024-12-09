import allure
from selenium import webdriver
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from final_project.helpers.functions import *


class MenuPage(Base):

    MENU_TAB = ("xpath", "//a[text()='Меню']")
    PAGE_NAME_1 = ("xpath", "//h1[text()='Меню']")
    DESSERT_TAB = ("xpath", "(//a[text()='Десерты'])[2]")
    PAGE_NAME_2 = ("xpath", "//h1[text()='Десерты']")
    PRICE_SLIDER_LEFT = ("xpath", "//*[@style='left: 100%;']")
    PRICE_BUTTON = ("xpath", "//div/button[@type='submit']")
    SLIDER_PRICE_SELECTED = ("xpath", "//span[@class='to']")
    SELECTED_PRICES = ("xpath", "//span/span/bdi")
    BUTTON_TO_CART = ("xpath", "//a[contains(@aria-label, 'Булочка с корицей')]")
    PRICE_DESSERT = (
        "xpath",
        "//a[contains(@aria-label, 'Булочка с корицей')]/preceding-sibling::span//bdi",
    )

    def menu_tab_click(self):
        with allure.step("Кликнуть по вкладке «Меню»"):
            self.wait.until(EC.element_to_be_clickable(self.MENU_TAB)).click()

    def is_menu_page(self):
        with allure.step("Проверить, что отображается страница «Меню»."):
            page_name = self.wait.until(
                EC.visibility_of_element_located(self.PAGE_NAME_1)
            )
            assert page_name.text.upper() == "МЕНЮ"

    def dessert_tab_click(self):
        with allure.step("Кликнуть раздел «Десерты»."):
            self.wait.until(EC.element_to_be_clickable(self.DESSERT_TAB)).click()

    def is_dessert_page(self):
        with allure.step("Проверить, что отображается страница «Десерты»."):
            page_name = self.wait.until(
                EC.visibility_of_element_located(self.PAGE_NAME_2)
            )
            assert page_name.text.upper() == "ДЕСЕРТЫ"

    def price_slider_move(self):
        with allure.step(
            "Сдвинуть правый ползунок слайдера влево до уменьшения ценового диапазона до 135 рублей "
            "включительно."
        ):
            element = self.wait.until(
                EC.visibility_of_element_located(self.PRICE_SLIDER_LEFT)
            )
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.click_and_hold(element).move_by_offset(
                xoffset=-223, yoffset=0
            ).perform()
            return action_chains.release().perform()

    def check_selected_price_level(self):
        with allure.step(
            "Проверить, что отображается ценовой диапазон по 135 рублей включительно."
        ):
            price_element = self.wait.until(
                EC.visibility_of_element_located(self.SLIDER_PRICE_SELECTED)
            )
            assert price_element.text == "135", "Ошибка: не верный ценовой диапазон."

    def submit_price_button_click(self):
        with allure.step("Нажать под слайдером кнопку 'Применить'."):
            self.wait.until(EC.element_to_be_clickable(self.PRICE_BUTTON)).click()

    def check_selected_prices_list(self):
        with allure.step(
            "Проверить, что отображаются десерты стоимостью 135 рублей и меньше."
        ):
            prices_list = self.driver.find_elements(*self.SELECTED_PRICES)
            assert compare_prices_with_selected_level(prices_list) is True

    def dessert_button_click(self):
        with allure.step(
            "Нажать кнопку 'В корзину' под изображением выбранного десерта."
        ):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_TO_CART)).click()

    def price_product_2(self):
        with allure.step("Найти цену товара, соответствующую выбранному десерту."):
            dessert_price = self.wait.until(
                EC.visibility_of_element_located(self.PRICE_DESSERT)
            ).text
            dessert_price_int = extract_figures(dessert_price)
            return dessert_price_int
