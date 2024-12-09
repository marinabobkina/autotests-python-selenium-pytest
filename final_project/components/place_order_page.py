import allure
import datetime
from datetime import datetime, timedelta  # noqa
from final_project.base.base import Base
from selenium.webdriver.support import expected_conditions as EC
from final_project.helpers.functions import *
from final_project.data.valid_data import ValidData


class PlaceOrderPage(Base, ValidData):

    PLACE_ORDER_TAB = ("xpath", "//a[text()='Оформление заказа']")
    PLACE_ORDER_PAGE = ("xpath", "//span[@class='current']")
    CHECK_AUTHORIZATION = ("xpath", "(//div[@class='woocommerce-info'])[1]")
    AUTHORIZATION_LINK = ("xpath", "//a[@class='showlogin']")
    CHECKBOX_REMEMBERME = ("xpath", "//input[@name='rememberme']")
    BUTTON_LOGIN = ("xpath", "//button[@name='login']")

    NAME_FIELD = ("xpath", "//input[@name='billing_first_name']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='billing_last_name']")
    ADDRESS_FIELD = ("xpath", "//input[@name='billing_address_1']")
    CITY_FIELD = ("xpath", "//input[@name='billing_city']")
    REGION_FIELD = ("xpath", "//input[@name='billing_state']")
    POSTCODE_FIELD = ("xpath", "//input[@name='billing_postcode']")
    PHONE_FIELD = ("xpath", "//input[@name='billing_phone']")
    DATE_FIELD = ("xpath", "//input[@name='order_date']")
    COMMENTS_FIELD = ("xpath", "//textarea[@name='order_comments']")
    RADIO_BUTTON = ("xpath", "(//input[@name='payment_method'])[2]")
    CHECKBOX_TERMS = ("xpath", "//input[@name='terms']")
    BUTTON_PLACE_ORDER = ("xpath", "//button[@id='place_order']")

    CONFIRM_ORDER = ("xpath", "//h2[text()='Заказ получен']")
    TOTAL_ORDER_AMOUNT = ("xpath", "(//td/span)[3]")
    PERSONAL_DATA = ("xpath", "//section/address")

    PLACE_ORDER_WINDOW = ("xpath", "//h2[@class='post-title']")
    INVALID_NAME_ALERT = ("xpath", "//li[@data-id='billing_first_name']")
    INVALID_LAST_NAME_ALERT = ("xpath", "//li[@data-id='billing_last_name']")
    INVALID_ADDRESS_ALERT = ("xpath", "//li[@data-id='billing_address_1']")
    INVALID_CITY_ALERT = ("xpath", "//li[@data-id='billing_city']")
    INVALID_REGION_ALERT = ("xpath", "//li[@data-id='billing_state']")
    INVALID_POSTCODE_ALERT = ("xpath", "//li[@data-id='billing_postcode']")
    INVALID_PHONE_ALERT = ("xpath", "//li[@data-id='billing_phone']")

    def place_order_tab_click(self):
        with allure.step("Кликнуть по вкладке «Оформление заказа»"):
            self.wait.until(EC.element_to_be_clickable(self.PLACE_ORDER_TAB)).click()

    def is_place_order_page(self):
        with allure.step("Проверить, что отображается страница «Оформление заказа»."):
            page_name = self.wait.until(
                EC.visibility_of_element_located(self.PLACE_ORDER_PAGE)
            )
            assert page_name.text == "Оформление Заказа", (
                "Ошибка: название страницы не соответствует 'Оформление " "Заказа'."
            )

    def check_authorization(self):
        with allure.step(
            "Проверить, что отображается сообщение 'Зарегистрированы на сайте? Авторизуйтесь'."
        ):
            text = self.wait.until(
                EC.visibility_of_element_located(self.CHECK_AUTHORIZATION)
            ).text
            assert text == "Зарегистрированы на сайте? Авторизуйтесь", (
                "Ошибка: текст сообщения не соответствует "
                "'Зарегистрированы на сайте? Авторизуйтесь'."
            )

    def authorization_link_click(self):
        with allure.step("Кликнуть по ссылке «Авторизуйтесь»."):
            self.wait.until(EC.element_to_be_clickable(self.AUTHORIZATION_LINK)).click()

    def checkbox_rememberme_click(self):
        with allure.step("Кликнуть по чекбоксу «Запомнить меня»."):
            self.wait.until(
                EC.element_to_be_clickable(self.CHECKBOX_REMEMBERME)
            ).click()

    def button_login_click(self):
        with allure.step("Кликнуть по кнопке «Войти»."):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_LOGIN)).click()

    def send_data_in_name_field(self, name):
        with allure.step("Заполнить поле «Имя»."):
            self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)

    def clear_data_in_name_field(self):
        with allure.step("Очистить поле «Имя»."):
            self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).clear()

    def check_name_in_name_field(self):
        with allure.step("Заполнить поле 'Имя' валидным значением."):
            name = self.wait.until(
                EC.visibility_of_element_located(self.NAME_FIELD)
            ).get_attribute("value")
            if name != self.NAME_1:
                self.clear_data_in_name_field()
                self.send_data_in_name_field(self.NAME_1)

    def send_data_in_last_name_field(self, last_name):
        with allure.step("Заполнить поле «Фамилия»."):
            self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(
                last_name
            )

    def clear_data_in_last_name_field(self):
        with allure.step("Очистить поле «Фамилия»."):
            self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).clear()

    def check_last_name_in_last_name_field(self):
        with allure.step("Заполнить поле 'Фамилия' валидным значением."):
            last_name = self.wait.until(
                EC.visibility_of_element_located(self.LAST_NAME_FIELD)
            ).get_attribute("value")
            if last_name != self.LAST_NAME_1:
                self.clear_data_in_last_name_field()
                self.send_data_in_last_name_field(self.LAST_NAME_1)

    def send_data_in_address_field(self, address):
        with allure.step("Заполнить поле «Адрес»."):
            self.wait.until(EC.element_to_be_clickable(self.ADDRESS_FIELD)).send_keys(
                address
            )

    def clear_data_in_address_field(self):
        with allure.step("Очистить поле «Адрес»."):
            self.wait.until(EC.element_to_be_clickable(self.ADDRESS_FIELD)).clear()

    def check_address_in_address_field(self):
        with allure.step("Заполнить поле 'Адрес' валидным значением."):
            address = self.wait.until(
                EC.visibility_of_element_located(self.ADDRESS_FIELD)
            ).get_attribute("value")
            if address != self.ADDRESS_1:
                self.clear_data_in_address_field()
                self.send_data_in_address_field(self.ADDRESS_1)

    def send_data_in_city_field(self, city):
        with allure.step("Заполнить поле «Город / Населенный пункт»."):
            self.wait.until(EC.element_to_be_clickable(self.CITY_FIELD)).send_keys(city)

    def clear_data_in_city_field(self):
        with allure.step("Очистить поле «Город / Населенный пункт»."):
            self.wait.until(EC.element_to_be_clickable(self.CITY_FIELD)).clear()

    def check_city_in_city_field(self):
        with allure.step(
            "Заполнить поле 'Город / Населенный пункт' валидным значением."
        ):
            city = self.wait.until(
                EC.visibility_of_element_located(self.CITY_FIELD)
            ).get_attribute("value")
            if city != self.CITY_1:
                self.clear_data_in_city_field()
                self.send_data_in_city_field(self.CITY_1)

    def send_data_in_region_field(self, region):
        with allure.step("Заполнить поле «Область»."):
            self.wait.until(EC.element_to_be_clickable(self.REGION_FIELD)).send_keys(
                region
            )

    def clear_data_in_region_field(self):
        with allure.step("Очистить поле «Область»."):
            self.wait.until(EC.element_to_be_clickable(self.REGION_FIELD)).clear()

    def check_region_in_region_field(self):
        with allure.step("Заполнить поле 'Область' валидным значением."):
            region = self.wait.until(
                EC.visibility_of_element_located(self.REGION_FIELD)
            ).get_attribute("value")
            if region != self.REGION_1:
                self.clear_data_in_region_field()
                self.send_data_in_region_field(self.REGION_1)

    def send_data_in_postcode_field(self, postcode):
        with allure.step("Заполнить поле «Почтовый индекс»."):
            self.wait.until(EC.element_to_be_clickable(self.POSTCODE_FIELD)).send_keys(
                postcode
            )

    def clear_data_in_postcode_field(self):
        with allure.step("Очистить поле «Почтовый индекс»."):
            self.wait.until(EC.element_to_be_clickable(self.POSTCODE_FIELD)).clear()

    def check_postcode_in_postcode_field(self):
        with allure.step("Заполнить поле 'Почтовый индекс' валидным значением."):
            postcode = self.wait.until(
                EC.visibility_of_element_located(self.POSTCODE_FIELD)
            ).get_attribute("value")
            if postcode != self.POSTCODE_1:
                self.clear_data_in_postcode_field()
                self.send_data_in_postcode_field(self.POSTCODE_1)

    def send_data_in_phone_field(self, phone):
        with allure.step("Заполнить поле «Телефон»."):
            self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD)).send_keys(
                phone
            )

    def clear_data_in_phone_field(self):
        with allure.step("Очистить поле «Телефон»."):
            self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD)).clear()

    def check_phone_in_phone_field(self):
        with allure.step("Заполнить поле 'Телефон' валидным значением."):
            phone = self.wait.until(
                EC.visibility_of_element_located(self.PHONE_FIELD)
            ).get_attribute("value")
            if phone != self.PHONE_1:
                self.clear_data_in_phone_field()
                self.send_data_in_phone_field(self.PHONE_1)

    def choose_date_tomorrow(self):
        with allure.step("Установить в поле 'Дата заказа' завтрашнюю дату."):
            date_format = "%d.%m.%Y"
            date_now = datetime.now()
            date_tomorrow = date_now + timedelta(days=1)
            self.wait.until(EC.element_to_be_clickable(self.DATE_FIELD)).send_keys(
                date_tomorrow.strftime(date_format)
            )

    def check_date_tomorrow(self):
        with allure.step(
            "Проверить, что в поле 'Дата заказа' отображается выбранная дата."
        ):
            date_format = "%Y-%m-%d"
            date_tomorrow = (datetime.now() + timedelta(days=1)).strftime(date_format)
            calendar_date = self.wait.until(
                EC.visibility_of_element_located(self.DATE_FIELD)
            ).get_attribute("value")
            assert calendar_date == date_tomorrow

    def choose_date_yesterday(self):
        with allure.step("Установить в поле 'Дата заказа' вчерашнюю дату."):
            date_format = "%d.%m.%Y"
            date_now = datetime.now()
            date_yesterday = date_now - timedelta(days=1)
            self.wait.until(EC.element_to_be_clickable(self.DATE_FIELD)).send_keys(
                date_yesterday.strftime(date_format)
            )

    def check_date_yesterday(self):
        with allure.step(
            "Проверить, что в поле 'Дата заказа' отображается выбранная дата."
        ):
            date_format = "%Y-%m-%d"
            date_tomorrow = (datetime.now() - timedelta(days=1)).strftime(date_format)
            calendar_date = self.wait.until(
                EC.visibility_of_element_located(self.DATE_FIELD)
            ).get_attribute("value")
            assert calendar_date == date_tomorrow

    def write_comment(self):
        with allure.step("Написать комментарий в поле 'Комментарии к заказу'."):
            self.wait.until(EC.element_to_be_clickable(self.COMMENTS_FIELD)).send_keys(
                "привезти к 18:00/ by 6 p.m."
            )

    def check_comment(self):
        with allure.step(
            "Проверить, в поле 'Комментарии к заказу' отображается введенное значение."
        ):
            comment = self.wait.until(
                EC.visibility_of_element_located(self.COMMENTS_FIELD)
            ).get_attribute("value")
            assert comment == "привезти к 18:00/ by 6 p.m."

    def payment_button_click(self):
        with allure.step("Кликнуть по кнопке «Оплата при доставке»."):
            self.wait.until(EC.element_to_be_clickable(self.RADIO_BUTTON)).click()

    def payment_button_is_selected(self):
        with allure.step("Проверить, что радио-кнопка «Оплата при доставке» выбрана."):
            self.wait.until(EC.element_located_to_be_selected(self.RADIO_BUTTON))

    def checkbox_terms_click(self):
        with allure.step(
            "Кликнуть по чекбоксу, подтверждающему согласие с условиями сайта."
        ):
            self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_TERMS)).click()

    def checkbox_terms_is_selected(self):
        with allure.step(
            "Проверить, что чекбокс, подтверждающий согласие с условиями сайта, выбран."
        ):
            self.wait.until(EC.element_located_to_be_selected(self.CHECKBOX_TERMS))

    def button_place_order_click(self):
        with allure.step("Кликнуть по кнопке 'Оформить заказ'."):
            self.wait.until(EC.element_to_be_clickable(self.BUTTON_PLACE_ORDER)).click()

    def is_order_confirmed(self):
        with allure.step("Проверить, появилось ли подтверждение о получении заказа."):
            message = self.wait.until(
                EC.visibility_of_element_located(self.CONFIRM_ORDER)
            ).text.lower()
            assert (
                message == "заказ получен"
            ), "Не отображается окно с подтверждением заказа."

    def find_total_order_amount(self):
        with allure.step("Найти общую сумму заказа."):
            order_amount = self.wait.until(
                (EC.visibility_of_element_located(self.TOTAL_ORDER_AMOUNT))
            ).text
            order_amount_int = extract_figures(order_amount)
            return order_amount_int

    def check_personal_data(self):
        with allure.step(
            "Проверить, что личные данные в подтверждении заказа соответствуют введенным значениям."
        ):
            personal_data = self.wait.until(
                EC.visibility_of_element_located(self.PERSONAL_DATA)
            ).text
            assert self.NAME_1 in personal_data
            assert self.LAST_NAME_1 in personal_data
            assert self.ADDRESS_1 in personal_data
            assert self.CITY_1 in personal_data
            assert self.REGION_1 in personal_data
            assert self.POSTCODE_1 in personal_data
            assert self.PHONE_1 in personal_data

    def is_place_order_window(self):
        with allure.step(
            "Проверить, что отображается окно 'Оформление заказа' с полями для ввода личных данных."
        ):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    self.PLACE_ORDER_WINDOW, "ОФОРМЛЕНИЕ ЗАКАЗА"
                )
            )

    def is_window_name_changed(self):
        with allure.step(
            "Проверить, не изменилось ли окно 'Оформление заказа' на 'Заказ получен'."
        ):
            message = self.wait.until(
                EC.text_to_be_present_in_element(
                    self.PLACE_ORDER_WINDOW, "ЗАКАЗ ПОЛУЧЕН"
                )
            )
            assert (
                message is False
            ), "Окно 'Оформление заказа' изменилось на 'Заказ получен'."

    def is_error_message_visible(self):
        with allure.step(
            "Проверить, что отображаются сообщения о некорректных значениях в полях для ввода личных "
            "данных."
        ):
            name = self.wait.until(
                EC.visibility_of_element_located(self.INVALID_NAME_ALERT)
            ).text.lower()
            assert (
                "имя" in name
            ), "Сообщение о некорректном имени пользователя отсутствует."

            last_name = self.wait.until(
                EC.visibility_of_element_located(self.INVALID_LAST_NAME_ALERT)
            ).text.lower()
            assert (
                "фамилия" in last_name
            ), "Сообщение о некорректной фамилии пользователя отсутствует."

            address = self.wait.until(
                EC.visibility_of_element_located(self.INVALID_ADDRESS_ALERT)
            ).text.lower()
            assert (
                "адрес" in address
            ), "Сообщение о некорректном адресе пользователя отсутствует."

            city = self.wait.until(
                EC.visibility_of_element_located(self.INVALID_CITY_ALERT)
            ).text.lower()
            assert "город / населенный пункт" in city, (
                "Сообщение о некорректном городе/населенном пункте "
                "пользователя отсутствует."
            )

            region = self.wait.until(
                EC.visibility_of_element_located(self.INVALID_REGION_ALERT)
            ).text.lower()
            assert (
                "область" in region
            ), "Сообщение о некорректной области пользователя отсутствует."

            postcode = self.wait.until(
                EC.visibility_of_element_located(self.INVALID_POSTCODE_ALERT)
            ).text.lower()
            assert (
                "почтовый индекс" in postcode
            ), "Сообщение о некорректном почтовом индексе пользователя отсутствует."

            phone = self.wait.until(
                EC.visibility_of_element_located(self.INVALID_PHONE_ALERT)
            ).text.lower()
            assert (
                "телефон" in phone
            ), "Сообщение о некорректном телефоне пользователя отсутствует."

    def is_error_message_invisible(self):
        with allure.step(
            "Проверить, что сообщения о некорректных значениях в полях для ввода личных данных продолжают "
            "отображаться на странице."
        ):
            name = self.wait.until(
                EC.invisibility_of_element_located(self.INVALID_NAME_ALERT)
            )
            assert (
                name is False
            ), "Сообщение о некорректном имени пользователя отсутствует."

            last_name = self.wait.until(
                EC.invisibility_of_element_located(self.INVALID_LAST_NAME_ALERT)
            )
            assert (
                last_name is False
            ), "Сообщение о некорректной фамилии пользователя отсутствует."

            address = self.wait.until(
                EC.invisibility_of_element_located(self.INVALID_ADDRESS_ALERT)
            )
            assert (
                address is False
            ), "Сообщение о некорректном адресе пользователя отсутствует."

            city = self.wait.until(
                EC.invisibility_of_element_located(self.INVALID_CITY_ALERT)
            )
            assert (
                city is False
            ), "Сообщение о некорректном городе/населенном пункте пользователя отсутствует."

            region = self.wait.until(
                EC.invisibility_of_element_located(self.INVALID_REGION_ALERT)
            )
            assert (
                region is False
            ), "Сообщение о некорректной области пользователя отсутствует."

            postcode = self.wait.until(
                EC.invisibility_of_element_located(self.INVALID_POSTCODE_ALERT)
            )
            assert (
                postcode is False
            ), "Сообщение о некорректном почтовом индексе пользователя отсутствует."

            phone = self.wait.until(
                EC.invisibility_of_element_located(self.INVALID_PHONE_ALERT)
            )
            assert (
                phone is False
            ), "Сообщение о некорректном телефоне пользователя отсутствует."
