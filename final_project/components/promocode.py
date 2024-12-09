import allure

from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from final_project.helpers.functions import *


class Promocode(Base):

    SHOWCOUPON_LINK = ("xpath", "//a[@class='showcoupon']")
    COUPON_FIELD = ("xpath", "//input[@name='coupon_code']")
    BUTTON_APPLY_COUPON = ("xpath", "//button[@name='apply_coupon']")
    SUBTOTAL_AMOUNT = ("xpath", "//tr[@class='cart-subtotal']//bdi")
    DISCOUNT_AMOUNT = ("xpath", "(//tr[contains(@class, 'cart-discount')]//span)[1]")
    TOTAL_AMOUNT = ("xpath", "//tr[@class='order-total']//bdi")
    ERROR_COUPON_ALERT = ("xpath", "//ul[@role='alert']")
    CONFIRM_COUPON_ALERT = ("xpath", "//div[@role='alert']")

    def showcoupon_link_click(self):
        with allure.step("Кликнуть по ссылке «Нажмите для ввода купона»."):
            self.wait.until(EC.element_to_be_clickable(self.SHOWCOUPON_LINK)).click()

    def fill_coupon_field(self, coupon):
        with allure.step("Ввести в поле применения купона «GIVEMEHALYAVA»."):
            self.wait.until(EC.element_to_be_clickable(self.COUPON_FIELD)).send_keys(
                coupon
            )

    def apply_coupon_button_click(self):
        with allure.step("Кликнуть по кнопке «Применить купон»."):
            self.wait.until(
                EC.element_to_be_clickable(self.BUTTON_APPLY_COUPON)
            ).click()

    def find_subtotal_amount(self):
        with allure.step("Найти общую сумму заказа."):
            subtotal_amount = self.wait.until(
                EC.visibility_of_element_located(self.SUBTOTAL_AMOUNT)
            ).text
            subtotal_amount_int = extract_figures(subtotal_amount)
            return subtotal_amount_int

    def find_discount_amount(self):
        with allure.step("Найти сумму скидки."):
            discount_amount = self.wait.until(
                EC.visibility_of_element_located(self.DISCOUNT_AMOUNT)
            ).text
            discount_amount_int = extract_figures(discount_amount)
            return discount_amount_int

    def find_total_amount(self):
        with allure.step("Найти итоговую сумму заказа."):
            total_amount = self.wait.until(
                EC.visibility_of_element_located(self.TOTAL_AMOUNT)
            ).text
            total_amount_int = extract_figures(total_amount)
            return total_amount_int

    def is_discount_amount_10_percent(self):
        with allure.step(
            "Проверить, что сумма скидки составляет 10% от общей суммы заказа."
        ):
            assert (
                self.find_subtotal_amount() * 10 / 100
            ) == self.find_discount_amount()

    def check_total_amount(self):
        with allure.step(
            "Проверить, что итоговая сумма заказа уменьшилась на сумму скидки."
        ):
            assert (self.find_subtotal_amount() - self.find_total_amount()) == (
                self.find_discount_amount()
            )

    def check_error_coupon_alert(self):
        with allure.step("Проверить, что отображается сообщение 'Неверный купон.'."):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    self.ERROR_COUPON_ALERT, "Неверный купон."
                )
            )

    def check_failure_coupon_alert(self):
        with allure.step(
            "Проверить, что отображается сообщение о невозможности повторного применения купона."
        ):
            message = self.wait.until(
                EC.visibility_of_element_located(self.CONFIRM_COUPON_ALERT)
            ).text
            print("Уведомление об отказе в повторном применении промокода: ", message)
            assert (
                message != "Coupon code applied successfully."
            ), "Ошибка: купон применен повторно."

    def is_discount(self):
        with allure.step("Проверить, что скидка не была предоставлена."):
            assert self.find_subtotal_amount() == self.find_total_amount()

    def replace_response(self):
        self.apply_coupon_button_click()
        with allure.step("Дождаться и перехватить запрос на отправку купона."):
            request_wait = self.driver.wait_for_request("/?wc-ajax=apply_coupon")

        with allure.step("Заблокировать перехваченный запрос на отправку купона и вернуть ответ от "
                         "сервера с кодом '500'."):

            def block_request(request):
                if request_wait:
                    request.abort()
                    request.create_response(status_code=500)

            self.driver.request_interceptor = block_request
            self.open_page()

        with allure.step("Найти ответ от сервера с url 'https://pizzeria.skillbox.cc/' и статусом кода '500' и "
                         "напечатать ответ."):
            for request in self.driver.requests:
                if request.response:
                    if "https://pizzeria.skillbox.cc/" in request.url and request.response.status_code == 500:
                        print(request.response)
