import allure
from selenium import webdriver
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC  # noqa
from final_project.helpers.functions import *


class CartPage(Base):

    CART_TAB = ("xpath", "//a[text()='Корзина']")
    CART_PAGE = ("xpath", "//span[@class='current']")
    QUANTITY_FIELD = ("xpath", "//input[@title='Кол-во']")
    QUANTITY_FIELD_PRODUCT1 = ("xpath", "(//input[@title='Кол-во'])[1]")
    QUANTITY_FIELD_PRODUCT2 = ("xpath", "(//input[@title='Кол-во'])[2]")
    PRICE_FIELD_PRODUCT1 = ("xpath", "(//td[@class='product-subtotal']//bdi)[1]")
    PRICE_FIELD_PRODUCT2 = ("xpath", "(//td[@class='product-subtotal']//bdi)[2]")
    BUTTON_UPDATE_CART = ("xpath", "//button[@name='update_cart']")
    PRICE_SUBTOTAL = ("xpath", "//tr[@class='cart-subtotal']//bdi")
    PRICE_TOTAL = ("xpath", "//tr[@class='order-total']//bdi")
    REMOVE_ICON = ("xpath", "(//a[@class='remove'])[2]")
    ALERT = ("xpath", "//div[@role='alert']")

    def cart_tab_click(self):
        with allure.step("Кликнуть по вкладке «Корзина»"):
            self.wait.until(EC.element_to_be_clickable(self.CART_TAB)).click()

    def is_cart_page(self):
        with allure.step("Проверить, что отображается страница «Корзина»."):
            page_name = self.wait.until(
                EC.visibility_of_element_located(self.CART_PAGE)
            )
            assert (
                page_name.text == "Корзина"
            ), "Ошибка: название страницы не соответствует 'Корзина'."

    def check_quantity_product_1(self):
        with allure.step("Проверить, что количество первого товара равно '1'."):
            element = self.wait.until(
                EC.visibility_of_element_located(self.QUANTITY_FIELD_PRODUCT1)
            ).get_attribute("value")
            assert element == "1", "Ошибка: количество первого товара не равно '1'."

    def check_quantity_product_2(self):
        with allure.step("Проверить, что количество второго товара равно '1'."):
            element = self.wait.until(
                EC.visibility_of_element_located(self.QUANTITY_FIELD_PRODUCT2)
            ).get_attribute("value")
            assert element == "1", "Ошибка: количество второго товара не равно '1'."

    def find_price_in_cart_product_1(self):
        with allure.step("Найти цену первого товара в корзине."):
            price = self.wait.until(
                EC.visibility_of_element_located(self.PRICE_FIELD_PRODUCT1)
            ).text
            price_int = extract_figures(price)
            return price_int

    def find_price_in_cart_product_2(self):
        with allure.step("Найти цену второго товара в корзине."):
            price = self.wait.until(
                EC.visibility_of_element_located(self.PRICE_FIELD_PRODUCT2)
            ).text
            price_int = extract_figures(price)
            return price_int

    def increase_quantity(self):
        with allure.step("Увеличить количество первого товара на единицу."):
            element = self.wait.until(
                EC.visibility_of_element_located(self.QUANTITY_FIELD)
            )
            action_chains = webdriver.ActionChains(self.driver)
            action_chains.move_to_element_with_offset(
                element, xoffset=10, yoffset=-10
            ).click().perform()
            return action_chains

    def update_cart(self):
        with allure.step("Нажать на кнопку «Обновить корзину»."):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_UPDATE_CART)).click()

    def check_button_state(self):
        with allure.step("Проверить, что кнопка «Обновить корзину» стала не активной."):
            self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.BUTTON_UPDATE_CART, "aria-disabled", "true"
                )
            )

    def check_quantity_after_changing(self):
        with allure.step("Проверить, что количество первого товара равно '2'."):
            element = self.wait.until(
                EC.visibility_of_element_located(self.QUANTITY_FIELD_PRODUCT1)
            ).get_attribute("value")
            assert element == "2", "Ошибка: количество товара не равно '2'."

    def find_subtotal_price(self):
        with allure.step("Найти общую стоимость товаров в корзине."):
            price = self.wait.until(
                EC.visibility_of_element_located(self.PRICE_SUBTOTAL)
            ).text
            price_int = extract_figures(price)
            return price_int

    def find_total_order_price(self):
        with allure.step("Найти итоговую сумму заказа в корзине."):
            price = self.wait.until(
                EC.visibility_of_element_located(self.PRICE_TOTAL)
            ).text
            price_int = extract_figures(price)
            return price_int

    def remove_icon_click(self):
        with allure.step("Удалить вторую позицию в корзине."):
            self.wait.until(EC.element_to_be_clickable(self.REMOVE_ICON)).click()

    def check_invisibility_removed_product(self):
        with allure.step(
            "Проверить, что удаленная из корзины позиция не отображается."
        ):
            invisibility = self.wait.until(
                EC.invisibility_of_element_located(self.PRICE_FIELD_PRODUCT2)
            )
            assert (
                invisibility is True
            ), "Ошибка: удаленная из корзины позиция отображается на странице."

    def check_alert_text(self):
        with allure.step(
            "Проверить, что отображается уведомление об удаленном товаре с возможностью вернуть его."
        ):
            alert_text = self.wait.until(
                EC.visibility_of_element_located(self.ALERT)
            ).text
            assert alert_text == '“Десерт "Булочка с корицей"” удален. Вернуть?', (
                "Ошибка: не корректное уведомление" "об удаленном товаре."
            )
