import logging
import allure
from final_project.base.base_test import BaseTest
import time as t


@allure.feature("Тестирование флоу с бонусной системой.")
class TestBonus(BaseTest):
    @allure.story(
        "Вкладка «Бонусная программа»: ввод и активация данных, проверка оформления бонусной карты."
    )
    @allure.title("Регистрация в бонусной программе.")
    def test1_bonus_program_registration(self):

        logging.info("Открытие сайта.")
        self.bonus_page.open_page()

        logging.debug("Проверка, что открыт нужный сайт.")
        self.bonus_page.is_main_page()

        logging.info("Переход во вкладку 'Бонусная программа'.")
        logging.debug("Открытие вкладки 'Бонусная программа'.")
        self.bonus_page.bonus_page_click()

        logging.debug("Проверка, что отображается страница 'Бонусная программа'.")
        self.bonus_page.is_bonus_page()

        logging.info("Проверка отправки формы с незаполненными полями.")
        logging.debug("Кликнуть по кнопке 'Оформить карту'.")
        self.bonus_page.bonus_button_click()

        logging.debug(
            "Проверить, что появилось сообщение о не корректно заполненных полях формы."
        )
        self.bonus_page.check_error_message()

        logging.info("Проверка отправки формы с полями, заполненными пробелом.")
        logging.debug("Ввести пробел в поле 'Имя'.")
        t.sleep(3)
        self.bonus_page.enter_name(self.invalid_data.NAME)

        logging.debug("Ввести пробел в поле 'Телефон'.")
        self.bonus_page.enter_phone(self.invalid_data.PHONE)

        logging.debug("Кликнуть по кнопке 'Оформить карту'.")
        self.bonus_page.bonus_button_click()

        logging.debug(
            "Проверить, что появилось сообщение о не корректно заполненных полях формы."
        )
        self.bonus_page.check_error_message()

        logging.info("Ввод данных пользователя.")
        logging.debug("Ввести имя пользователя.")
        self.bonus_page.enter_name(self.valid_data.NAME)

        logging.debug("Проверить, что в поле 'Имя' отображается введенное значение.")
        self.bonus_page.check_name_in_field(self.valid_data.NAME)

        logging.debug("Ввести телефон пользователя.")
        self.bonus_page.enter_phone(self.valid_data.PHONE)

        logging.debug(
            "Проверить, что в поле 'Телефон' отображается введенное значение."
        )
        self.bonus_page.check_phone_in_field(self.valid_data.PHONE)

        logging.info("Отправка заполненной формы и проверка оформления бонусной карты.")
        logging.debug("Кликнуть по кнопке 'Оформить карту'.")
        self.bonus_page.bonus_button_click()

        logging.debug("Дождаться появления окна подтверждения и нажать 'ОК'.")
        self.bonus_page.click_confirm_alert()

        logging.debug("Проверить, что появилось сообщение об одобрении бонусной карты.")
        self.bonus_page.approval_bonus_card()
