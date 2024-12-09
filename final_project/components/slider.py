import allure
from selenium import webdriver
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from final_project.helpers.functions import *


class Slider(Base):

    MAIN_PAGE = ("xpath", "(//a[text()='Главная'])[1]")
    SLIDER_ELEMENT_1 = (
        "xpath",
        "//li[contains(@class, 'slick-active')]/div/a[contains(@title, 'Ветчина и грибы')]",
    )
    BUTTON_SELECTOR_1 = (
        "xpath",
        "//li[contains(@class, 'slick-active')]//a[contains(@aria-label, 'Ветчина и грибы')]",
    )
    SLIDER_ELEMENT_2 = (
        "xpath",
        "//li[contains(@class, 'slick-active')]/div/a[contains(@title, 'Как у бабушки')]",
    )
    BUTTON_SELECTOR_2 = (
        "xpath",
        "//li[contains(@class, 'slick-active')]//a[contains(@aria-label, 'Как у бабушки')]",
    )
    SLIDER_LEFT = ("class name", "slick-prev")
    SLIDER_RIGHT = ("class name", "slick-next")
    VISIBILITY_ELEMENT_1 = (
        "xpath",
        "(//a[contains(@title, 'Ветчина и грибы')])[3]/ancestor::li",
    )
    VISIBILITY_ELEMENT_NEW = (
        "xpath",
        "(//a[contains(@title, 'Пицца «Пепперони»')]/ancestor::li)[2]",
    )
    BUTTON_SELECTOR_NEW = (
        "xpath",
        "//li[contains(@class, 'slick-active')]//a[contains(@aria-label, 'Пепперони')]",
    )

    ELEMENT_VISIBLE = (
        "xpath",
        "//li[contains(@class, 'slick-active')]/a[contains(@title, 'Как у бабушки')]",
    )
    SLIDER_NAME = ("xpath", "(// a[contains( @ title, 'Как у бабушки')] /h3)[2]")
    SLIDER_PRICE = (
        "xpath",
        "(// a[contains( @ title, 'Как у бабушки')] / span / span)[2]",
    )

    SLIDER_PRICE_ELEMENT_1 = (
        "xpath",
        "(// a[contains( @ title, 'Ветчина и грибы')] / span / span)[2]",
    )

    def focus_element_1(self):
        with allure.step(
            "Навести мышку на крайнее справа изображение в слайдере (Пицца «Ветчина и грибы»)."
        ):
            element = self.wait.until(EC.element_to_be_clickable(self.SLIDER_ELEMENT_1))
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.move_to_element(element).perform()
            return action_chains

    def button1_is_visible(self):
        with allure.step("Дождаться появления кнопки «В корзину»."):
            button = self.wait.until(
                EC.visibility_of_element_located(self.BUTTON_SELECTOR_1)
            ).text
            assert button == "В КОРЗИНУ", "Ошибка: кнопка «В корзину» не отображается."

    def button1_click(self):
        with allure.step("Кликнуть на кнопку «В корзину»"):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_SELECTOR_1)).click()

    def slider_left_click(self):
        with allure.step("Кликнуть по левой кнопке слайдера."):
            element = self.wait.until(EC.element_to_be_clickable(self.SLIDER_LEFT))
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.move_to_element(element).click().perform()
            return action_chains

    def element_1_invisible_after_moving(self):
        with allure.step(
            "Проверить, что 'Пицца «Ветчина и грибы»' в слайдере сдвинулось после клика по левой кнопке "
            "слайдера и не отображается на странице."
        ):
            visibility_element = self.wait.until(
                EC.visibility_of_element_located(self.VISIBILITY_ELEMENT_1)
            )
            invisible_element = visibility_element.get_attribute("class")
            assert (
                "slick-active" not in invisible_element
            ), "Ошибка: слайдер отображается на странице."

    def focus_element_new_visible_after_moving(self):
        with allure.step(
            "Навести курсор на новое изображение в слайдере, появившиеся после клика по кнопке слайдера."
        ):
            check_element = self.wait.until(
                EC.element_to_be_clickable(self.VISIBILITY_ELEMENT_NEW)
            )
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.move_to_element(check_element).perform()
            return action_chains

    def button_new_is_visible(self):
        with allure.step(
            "Проверить, что появилась кнопка «В корзину» после фокусирования на новом изображении."
        ):
            button = self.wait.until(
                EC.visibility_of_element_located(self.BUTTON_SELECTOR_NEW)
            ).text
            assert button == "В КОРЗИНУ", "Ошибка: кнопка «В корзину» не отображается."

    def slider_right_click(self):
        with allure.step("Кликнуть по правой кнопке слайдера."):
            element = self.wait.until(EC.element_to_be_clickable(self.SLIDER_RIGHT))
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.move_to_element(element).click().perform()
            return action_chains

    def element_1_visible_after_moving(self):
        with allure.step(
            "Проверить, что 'Пицца «Ветчина и грибы»' снова отображается в слайдере."
        ):
            visibility_element = self.wait.until(
                EC.element_to_be_clickable(self.VISIBILITY_ELEMENT_1)
            )
            visible_element = visibility_element.get_attribute("class")
            assert (
                "slick-active" in visible_element
            ), "Ошибка: слайдер НЕ отображается на странице."

    def focus_element_2(self):
        with allure.step("Навести мышку на другое изображение с пиццей в слайдере."):
            element = self.wait.until(EC.element_to_be_clickable(self.SLIDER_ELEMENT_2))
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.move_to_element(element).perform()
            return action_chains

    def button2_is_visible(self):
        with allure.step(
            "Дождаться появления кнопки «В корзину» в выбранном другом слайдере."
        ):
            button = self.wait.until(
                EC.visibility_of_element_located(self.BUTTON_SELECTOR_2)
            ).text
            assert button == "В КОРЗИНУ", "Ошибка: кнопка «В корзину» не отображается."

    def button2_click(self):
        with allure.step(
            "Кликнуть на кнопку «В корзину», соответствующую выбранному другому слайдеру"
        ):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_SELECTOR_2)).click()

    def slider_name(self):
        with allure.step("Найти название пиццы, соответствующее выбранному слайдеру."):
            slider_name = self.wait.until(
                EC.visibility_of_element_located(self.SLIDER_NAME)
            ).text
            return slider_name

    def slider_price(self):
        with allure.step("Найти цену пиццы, соответствующую выбранному слайдеру."):
            slider_price = self.wait.until(
                EC.visibility_of_element_located(self.SLIDER_PRICE)
            ).text
            slider_price_int = extract_figures(slider_price)
            return slider_price_int

    def element_click(self):
        with allure.step("Нажать на выбранную картинку пиццы в слайдере."):
            self.wait.until(EC.element_to_be_clickable(self.ELEMENT_VISIBLE)).click()

    def price_product_1(self):
        with allure.step("Найти цену пиццы, соответствующую выбранному слайдеру."):
            slider_price = self.wait.until(
                EC.visibility_of_element_located(self.SLIDER_PRICE_ELEMENT_1)
            ).text
            slider_price_int = extract_figures(slider_price)
            return slider_price_int

    def main_page_click(self):
        with allure.step("Кликнуть по вкладке меню 'Главная'."):
            self.wait.until(EC.element_to_be_clickable(self.MAIN_PAGE)).click()
