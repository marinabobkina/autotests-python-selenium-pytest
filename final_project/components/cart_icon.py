import allure
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC


class CartIcon(Base):

    CART_PRICE = ("xpath", "//a[@title='View your shopping cart']")

    def change_price_in_cart(self):
        with allure.step(
            "Проверить, что сумма возле иконки корзины равна стоимости выбранной пиццы."
        ):
            price = self.wait.until(
                EC.text_to_be_present_in_element(self.CART_PRICE, "[ 450,00₽ ]")
            )
            if price is True:
                print("Cумма заказа равна стоимости выбранной пиццы.")
            else:
                print("Cумма заказа НЕ равна стоимости выбранной пиццы.")
            return price

    def cart_summ(self):
        with allure.step(
            "Проверить, что сумма возле иконки корзины равна стоимости двух выбранных пицц."
        ):
            summ = self.wait.until(
                EC.text_to_be_present_in_element(self.CART_PRICE, "[ 930,00₽ ]")
            )
            if summ is True:
                print("Cумма заказа равна стоимости двух выбранных пицц.")
            else:
                print("Cумма заказа НЕ равна стоимости двух выбранных пицц.")
            return summ

    def check_cart_icon_price(self):
        with allure.step(
            "Проверить, что сумма возле иконки корзины равна стоимости пиццы с дополнительной опцией."
        ):
            price = self.wait.until(
                EC.text_to_be_present_in_element(self.CART_PRICE, "[ 535,00₽ ]")
            )
            if price is True:
                print("Cумма заказа равна стоимости пиццы с дополнительной опцией.")
            else:
                print("Cумма заказа НЕ равна стоимости пиццы с дополнительной опцией.")
            return price

    def get_cart_icon_price(self):
        with allure.step(
            "Проверить, что сумма возле иконки корзины равна стоимости выбранного десерта."
        ):
            price = self.wait.until(
                EC.text_to_be_present_in_element(self.CART_PRICE, "[ 115,00₽ ]")
            )
            if price is True:
                print(
                    "Возле иконки тележки отображается стоимость добавленного десерта."
                )
            else:
                print("Cумма заказа НЕ равна стоимости добавленного десерта.")
            return price

    def check_two_products_summ(self):
        with allure.step(
            "Проверить, что сумма возле иконки корзины равна стоимости двух выбранных товаров."
        ):
            price = self.wait.until(
                EC.text_to_be_present_in_element(self.CART_PRICE, "[ 565,00₽ ]")
            )
            if price is True:
                print(
                    "Возле иконки тележки отображается стоимость двух выбранных товаров."
                )
            else:
                print("Cумма заказа НЕ равна стоимости двух выбранных товаров.")
            return price

    def cart_icon_click(self):
        with allure.step("Кликнуть иконку тележки в верхней части экрана."):
            self.wait.until(EC.element_to_be_clickable(self.CART_PRICE)).click()

    def check_price_in_cart(self):
        with allure.step(
            "Проверить, что сумма возле иконки корзины равна стоимости выбранной пиццы."
        ):
            self.wait.until(
                EC.text_to_be_present_in_element(self.CART_PRICE, "[ 480,00₽ ]")
            )
