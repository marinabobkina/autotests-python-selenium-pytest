import allure
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from final_project.data.valid_data import ValidData


class BonusPage(Base, ValidData):

    BONUS_PAGE = ("xpath", "(//a[text()='Бонусная программа'])[1]")
    NAME_PAGE = ("xpath", "//div[@id='accesspress-breadcrumb']/span")
    NAME_FIELD = ("xpath", "//input[@name='username']")
    PHONE_FIELD = ("xpath", "//input[@name='billing_phone']")
    BUTTON = ("xpath", "//button[@name='bonus']")
    BONUS_CONFIRM = ("xpath", "//div[@id='bonus_main']/h3")
    BONUS_CONTENT = ("xpath", "//div[@id='bonus_content']")

    def bonus_page_click(self):
        with allure.step("Кликнуть по вкладке меню 'Бонусная программа'."):
            self.wait.until(EC.element_to_be_clickable(self.BONUS_PAGE)).click()

    def is_bonus_page(self):
        with allure.step("Проверить, что отображается страница 'Бонусная программа'."):
            page_name = self.wait.until(
                EC.visibility_of_element_located(self.NAME_PAGE)
            ).text.lower()
            assert (
                page_name == "бонусная программа"
            ), "Ошибка: отображается не та страница."

    def enter_name(self, name):
        with allure.step("Ввести имя пользователя."):
            self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)

    def check_name_in_field(self, name):
        with allure.step(
            "Проверить, что в поле 'Имя' отображается введенное значение."
        ):
            check_name = self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.NAME_FIELD, "value", name
                )
            )
            assert (
                check_name is True
            ), f"Ошибка: имя пользователя не соответствует {name}."

    def enter_phone(self, phone):
        with allure.step("Ввести телефон пользователя."):
            self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD)).send_keys(
                phone
            )

    def check_phone_in_field(self, phone):
        with allure.step(
            "Проверить, что в поле 'Телефон' отображается введенное значение."
        ):
            check_phone = self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.PHONE_FIELD, "value", phone
                )
            )
            assert (
                check_phone is True
            ), f"Ошибка: телефон пользователя не соответствует {phone}."

    def bonus_button_click(self):
        with allure.step("Кликнуть по кнопке 'Оформить карту'."):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON)).click()

    def wait_alert(self):
        with allure.step(
            "Дождаться появления окна с запросом на подтверждение действия на сайте."
        ):
            self.wait.until(EC.alert_is_present())

    def click_confirm_alert(self):
        with allure.step("Нажать 'ОК' в появившемся окне подтверждения."):
            self.wait_alert()
            self.driver.switch_to.alert.accept()

    def approval_bonus_card(self):
        with allure.step(
            "Проверить, что появилось сообщение об одобрении бонусной карты."
        ):
            message = self.wait.until(
                EC.visibility_of_element_located(self.BONUS_CONFIRM)
            ).text
            print(message)
            assert (
                message == "Ваша карта оформлена!"
            ), "Сообщение не соответствует 'Ваша карта оформлена!'."

    def check_error_message(self):
        with allure.step(
            "Проверить, что появилось сообщение о не корректно заполненных полях формы."
        ):
            message = self.wait.until(
                EC.visibility_of_element_located(self.BONUS_CONTENT)
            ).text
            print(message)
            assert "Имя" in message, "В сообщении не упоминается 'Имя'."
            assert "Телефон" in message, "В сообщении не упоминается 'Телефон'."
