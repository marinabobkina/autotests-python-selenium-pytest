import allure
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from final_project.data.valid_data import ValidData


class MyAccountPage(Base, ValidData):

    MY_ACCOUNT_TAB = ("xpath", "//a[text()='Мой аккаунт']")
    REGISTRATION_TAB = ("xpath", "//a[text()='Регистрация']")
    MY_ACCOUNT_PAGE = ("xpath", "//span[@class='current']")
    BUTTON_REGISTRATION = ("xpath", "//button[text()='Зарегистрироваться']")
    WINDOW_REGISTRATION = ("xpath", "//h2[@class='post-title']")
    USERNAME_FIELD = ("id", "reg_username")
    USERNAME_AUTHORIZATION = ("id", "username")
    EMAIL_FIELD = ("id", "reg_email")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    BUTTON_SUBMIT = ("xpath", "//button[@name='register']")
    REGISTRATION_TEXT = ("xpath", "//div[text()='Регистрация завершена']")
    USERNAME = ("xpath", "//div[@class='woocommerce-MyAccount-content']//strong")
    ERROR_ALERT = ("xpath", "//strong[text()='Error:']/ancestor::li")
    BUTTON_LOGIN = ("xpath", "//button[@name='login']")

    def my_account_tab_click(self):
        with allure.step("Кликнуть по вкладке «Мой аккаунт»."):
            self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT_TAB)).click()

    def registration_tab_click(self):
        with allure.step("Кликнуть по вкладке «Регистрация»."):
            self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_TAB)).click()

    def is_my_account_page(self):
        with allure.step("Проверить, что отображается страница «Мой аккаунт»."):
            page_name = self.wait.until(
                EC.visibility_of_element_located(self.MY_ACCOUNT_PAGE)
            )
            assert (
                page_name.text == "Мой Аккаунт"
            ), "Ошибка: название страницы не соответствует 'Мой Аккаунт'."

    def button_registration_click(self):
        with allure.step("Нажать кнопку 'Зарегистрироваться'."):
            self.wait.until(
                EC.element_to_be_clickable(self.BUTTON_REGISTRATION)
            ).click()

    def is_registration_window(self):
        with allure.step("Проверить, что отображается окно «Регистрация»."):
            window_name = self.wait.until(
                EC.visibility_of_element_located(self.WINDOW_REGISTRATION)
            )
            assert (
                window_name.text.upper() == "РЕГИСТРАЦИЯ"
            ), "Ошибка: название окна не соответствует 'РЕГИСТРАЦИЯ'."

    def enter_login(self, login):
        with allure.step("Ввести имя пользователя."):
            self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    def enter_login_for_authorization(self, login):
        with allure.step("Ввести имя пользователя."):
            self.wait.until(EC.element_to_be_clickable(self.USERNAME_AUTHORIZATION)).send_keys(login)

    def check_login_in_input(self, login):
        with allure.step(
            "Проверить, что в поле 'имя пользователя' отображается введенное значение."
        ):
            name = self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.USERNAME_FIELD, "value", login
                )
            )
            assert name is True, f"Ошибка: имя пользователя не соответствует {login}."

    def enter_email(self, email):
        with allure.step("Ввести адрес электронной почты."):
            self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(
                email
            )

    def check_email_in_input(self, email):
        with allure.step(
            "Проверить, что в поле 'Адрес почты' отображается введенное значение."
        ):
            address = self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.EMAIL_FIELD, "value", email
                )
            )
            assert (
                address is True
            ), f"Ошибка: имя пользователя не соответствует {email}."

    def enter_password(self, password):
        with allure.step("Ввести пароль."):
            self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(
                password
            )

    def check_password_in_input(self, password):
        with allure.step(
            "Проверить, что в поле 'Пароль' отображается введенное значение."
        ):
            word = self.wait.until(
                EC.text_to_be_present_in_element_attribute(
                    self.PASSWORD_FIELD, "value", password
                )
            )
            assert (
                word is True
            ), f"Ошибка: имя пользователя не соответствует {password}."

    def click_submit_button(self):
        with allure.step("Нажать кнопку 'Зарегистрироваться'."):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_SUBMIT)).click()

    def is_registration_finished(self):
        with allure.step(
            "Проверить, что отображается сообщение «Регистрация завершена»."
        ):
            text = self.wait.until(
                EC.visibility_of_element_located(self.REGISTRATION_TEXT)
            ).text
            assert (
                text == "Регистрация завершена"
            ), "Ошибка: сообщение не соответствует 'Регистрация завершена'."

    def check_authorization(self, login):
        with allure.step(
            "Проверить, что имя пользователя в окне 'Мой аккаунт' соответствует введенному при регистрации"
            " значению в поле 'Имя пользователя'."
        ):
            user_name = self.wait.until(
                EC.visibility_of_element_located(self.USERNAME)
            ).text
            assert (
                user_name == login
            ), f"Ошибка: имя пользователя не соответствует '{login}'."

    def check_error_message_for_username_field(self):
        with allure.step(
            "Проверить корректность сообщения в ответ на ввод НЕ валидного имени пользователя."
        ):
            message = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_ALERT)
            ).text
            print("Текущее уведомление об ошибке: ", message)
            assert (
                message == "Error: Пожалуйста введите корректное имя пользователя."
            ), "Уведомление об ошибке в имени пользователя отсутствует или некорректное."

    def check_error_message_for_email_field(self):
        with allure.step(
            "Проверить корректность сообщения в ответ на ввод НЕ валидного адреса почты."
        ):
            message = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_ALERT)
            ).text
            print("Текущее уведомление об ошибке: ", message)
            assert (
                message == "Error: Пожалуйста, введите корректный email."
            ), "Уведомление об ошибке в адресе почты отсутствует или некорректное."

    def check_error_message_for_password_field(self):
        with allure.step(
            "Проверить корректность сообщения в ответ на ввод НЕ надежного пароля."
        ):
            message = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_ALERT)
            ).text
            print("Текущее уведомление об ошибке: ", message)
            assert (
                message == "Error: Введите корректный пароль для регистрации."
            ), "Уведомление об ошибке в поле 'Пароль' отсутствует или некорректное."

    def username_field_clear(self):
        with allure.step("Очистить поле 'Имя пользователя'."):
            self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).clear()

    def email_field_clear(self):
        with allure.step("Очистить поле 'Адрес почты'."):
            self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).clear()

    def button_login_click(self):
        with allure.step("Кликнуть по кнопке «Войти»."):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_LOGIN)).click()

    def wait_alert_tooltip_for_username_fild(self):
        with allure.step(
            "Проверить появление подсказки касательно корректных символов для поля 'Имя пользователя'."
        ):
            username_tooltip = self.wait.until(
                EC.presence_of_element_located(self.USERNAME_FIELD)
            )
            tooltip_text = username_tooltip.get_attribute("validationMessage").lower()
            print(tooltip_text)
            assert (
                "имя" in tooltip_text
            ), "Уведомление с подсказкой отсутствует или не касается имени пользователя."

    def wait_alert_tooltip_for_email_fild(self):
        with allure.step("Проверить появление подсказки."):
            email_tooltip = self.wait.until(
                EC.presence_of_element_located(self.EMAIL_FIELD)
            )
            tooltip_text = email_tooltip.get_attribute("validationMessage").lower()
            print(tooltip_text)
            assert "адрес" in tooltip_text, (
                "Уведомление с подсказкой отсутствует или не касается адреса электронной "
                "почты."
            )
