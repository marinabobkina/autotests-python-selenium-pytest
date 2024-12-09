import logging
import allure
from final_project.base.base_test import BaseTest


@allure.feature("Тестирование флоу с промокодом.")
class TestPromocode(BaseTest):
    @allure.story(
        "Вкладка «Оформление заказа»: добавление валидного промокода, применение скидки."
    )
    @allure.title(
        "Проверка получения 10%-ной скидки при применении промокода 'GIVEMEHALYAVA'."
    )
    def test1_get_discount_using_valid_promocode(self):

        logging.info("Открытие сайта.")  # noqa
        self.slider.open_page()

        logging.debug("Проверка, что открыт нужный сайт.")
        self.slider.is_main_page()

        logging.info("Добавление первого товара в корзину.")
        logging.debug("Фокус на одном из товаров в слайдере.")
        self.slider.focus_element_1()

        logging.debug("Ожидание появления кнопки 'В корзину'.")
        self.slider.button1_is_visible()

        logging.debug("Клик по кнопке 'В корзину'.")
        self.slider.button1_click()

        logging.info("Добавление второго товара в корзину.")
        logging.debug("Фокус на одном из товаров в слайдере.")
        self.slider.focus_element_2()

        logging.debug("Ожидание появления кнопки 'В корзину'.")
        self.slider.button2_is_visible()

        logging.debug("Клик по кнопке 'В корзину'.")
        self.slider.button2_click()

        logging.info("Переход на вкладку «Мой аккаунт».")  # noqa
        logging.debug("Клик по вкладке «Мой аккаунт».")
        self.my_account_page.my_account_tab_click()

        logging.debug("Проверка, что отображается страница «Мой аккаунт».")
        self.my_account_page.is_my_account_page()

        logging.info("Переход в окно регистрации.")
        logging.debug("Нажать кнопку «Зарегистрироваться».")
        self.my_account_page.button_registration_click()

        logging.debug("Проверка, что отображается окно «Регистрация».")
        self.my_account_page.is_registration_window()

        logging.info("Заполнение формы регистрации валидными значениями.")
        logging.debug("Ввод валидного имени пользователя.")
        self.my_account_page.enter_login(self.valid_data.USER_NAME_3)

        logging.debug(
            "Проверка, что в поле 'Имя пользователя' отображается введенное значение."
        )
        self.my_account_page.check_login_in_input(self.valid_data.USER_NAME_3)

        logging.debug("Ввод валидного адреса электронной почты.")
        self.my_account_page.enter_email(self.valid_data.EMAIL_ADDRESS_3)

        logging.debug(
            "Проверка, что в поле 'Адрес почты' отображается введенное значение."
        )
        self.my_account_page.check_email_in_input(self.valid_data.EMAIL_ADDRESS_3)

        logging.debug("Ввод валидного пароля.")
        self.my_account_page.enter_password(self.valid_data.PASSWORD_3)

        logging.debug("Проверка, что в поле 'Пароль' отображается введенное значение.")
        self.my_account_page.check_password_in_input(self.valid_data.PASSWORD_3)

        logging.info("Отправка заполненной формы регистрации.")
        logging.debug("Нажать кнопку 'Зарегистрироваться'.")
        self.my_account_page.click_submit_button()

        logging.info("Переход на вкладку «Оформление заказа».")  # noqa
        logging.debug("Клик по вкладке «Оформление заказа».")
        self.place_order_page.place_order_tab_click()

        logging.debug("Проверка, что отображается страница «Оформление заказа».")
        self.place_order_page.is_place_order_page()

        logging.info("Применение купона «GIVEMEHALYAVA».")
        logging.debug("Клик по ссылке «Нажмите для ввода купона».")
        self.promocode.showcoupon_link_click()

        logging.debug("Ввод в поле применения купона «GIVEMEHALYAVA».")
        self.promocode.fill_coupon_field(self.valid_data.COUPON_NAME)

        logging.debug("Кликнуть по кнопке «Применить купон».")
        self.promocode.apply_coupon_button_click()

        logging.info("Проверка, что конечная сумма заказа уменьшилась на 10%.")
        logging.debug(
            "Проверить, что сумма скидки составляет 10% от общей суммы заказа."
        )
        self.promocode.is_discount_amount_10_percent()

        logging.debug(
            "Проверить, что итоговая сумма заказа уменьшилась на сумму скидки."
        )
        self.promocode.check_total_amount()

    @allure.story(
        "Вкладка «Оформление заказа»: добавление НЕ валидного промокода, проверка предоставления скидки."
    )
    @allure.title(
        "Проверка предоставления скидки при применении НЕ валидного промокода 'DC120'."
    )
    def test2_use_invalid_promocode(self):

        logging.info("Открытие сайта.")  # noqa
        self.slider.open_page()

        logging.debug("Проверка, что открыт нужный сайт.")
        self.slider.is_main_page()

        logging.info("Добавление товара в корзину.")
        logging.debug("Фокус на одном из товаров в слайдере.")
        self.slider.focus_element_1()

        logging.debug("Ожидание появления кнопки 'В корзину'.")
        self.slider.button1_is_visible()

        logging.debug("Клик по кнопке 'В корзину'.")
        self.slider.button1_click()

        logging.debug(
            "Проверить, что сумма возле иконки тележки равна стоимости выбранного товара."
        )
        self.cart_icon.change_price_in_cart()

        logging.info("Переход на вкладку «Оформление заказа».")  # noqa
        logging.debug("Клик по вкладке «Оформление заказа».")
        self.place_order_page.place_order_tab_click()

        logging.debug("Проверка, что отображается страница «Оформление заказа».")
        self.place_order_page.is_place_order_page()

        logging.info("Выполнение авторизации.")
        logging.debug("Клик по по ссылке «Авторизуйтесь».")
        self.place_order_page.authorization_link_click()

        logging.debug("Ввод имени пользователя, использованного ранее при регистрации.")
        self.my_account_page.enter_login(self.valid_data.USER_NAME_3)

        logging.debug("Ввод пароля, использованного ранее при регистрации.")
        self.my_account_page.enter_password(self.valid_data.PASSWORD_3)

        logging.debug("Кликнуть по чекбоксу «Запомнить меня».")
        self.place_order_page.checkbox_rememberme_click()

        logging.debug("Кликнуть по кнопке «Войти».")
        self.place_order_page.button_login_click()

        logging.info("Переход на вкладку «Оформление заказа».")
        logging.debug("Клик по вкладке «Оформление заказа».")
        self.place_order_page.place_order_tab_click()

        logging.debug("Проверка, что отображается страница «Оформление заказа».")
        self.place_order_page.is_place_order_page()

        logging.info("Применение НЕ валидного купона «DC120».")
        logging.debug("Клик по ссылке «Нажмите для ввода купона».")
        self.promocode.showcoupon_link_click()

        logging.debug("Ввод в поле применения купона «DC120».")
        self.promocode.fill_coupon_field(self.invalid_data.INVALID_COUPON)

        logging.debug("Кликнуть по кнопке «Применить купон».")
        self.promocode.apply_coupon_button_click()

        logging.info(
            "Проверка, что НЕ валидный купон не был принят и скидка не предоставлена."
        )
        logging.debug("Проверить, что отображается сообщение 'Неверный купон.'")
        self.promocode.check_error_coupon_alert()

        logging.debug(
            "Проверить, что общая стоимость заказа равна итоговой сумме заказа."
        )
        self.promocode.is_discount()

    @allure.story(
        "Вкладка «Оформление заказа»: добавление валидного промокода, проверка предоставления скидки при "
        "блокировке ответа с сервера."
    )
    @allure.title("Проверка применения промокода в случае ошибки на стороне сервера.")
    def test3_using_promocode_with_server_error(self):

        logging.info("Открытие сайта.")  # noqa
        self.slider.open_page()

        logging.debug("Проверка, что открыт нужный сайт.")
        self.slider.is_main_page()

        logging.info("Добавление товара в корзину.")
        logging.debug("Фокус на одном из товаров в слайдере.")
        self.slider.focus_element_1()

        logging.debug("Ожидание появления кнопки 'В корзину'.")
        self.slider.button1_is_visible()

        logging.debug("Клик по кнопке 'В корзину'.")
        self.slider.button1_click()

        logging.debug(
            "Проверить, что сумма возле иконки тележки равна стоимости выбранного товара."
        )
        self.cart_icon.change_price_in_cart()

        logging.info(
            "Переход на вкладку «Оформление заказа» для выполнения авторизации."
        )
        logging.debug("Клик по вкладке «Оформление заказа».")
        self.place_order_page.place_order_tab_click()

        logging.debug("Проверка, что отображается страница «Оформление заказа».")
        self.place_order_page.is_place_order_page()

        logging.debug("Клик по по ссылке «Авторизуйтесь».")
        self.place_order_page.authorization_link_click()

        logging.debug("Ввод имени пользователя, использованного ранее при регистрации.")
        self.my_account_page.enter_login(self.valid_data.USER_NAME_3)

        logging.debug("Ввод пароля, использованного ранее при регистрации.")
        self.my_account_page.enter_password(self.valid_data.PASSWORD_3)

        logging.debug("Кликнуть по кнопке «Войти».")
        self.place_order_page.button_login_click()

        logging.info("Переход на вкладку «Оформление заказа» для применения купона.")
        logging.debug("Клик по вкладке «Оформление заказа».")
        self.place_order_page.place_order_tab_click()

        logging.debug("Проверка, что отображается страница «Оформление заказа».")
        self.place_order_page.is_place_order_page()

        logging.debug("Клик по ссылке «Нажмите для ввода купона».")
        self.promocode.showcoupon_link_click()

        logging.debug("Ввод в поле применения купона «GIVEMEHALYAVA».")
        self.promocode.fill_coupon_field(self.valid_data.COUPON_NAME)

        logging.info(
            "Перехват и блокировка запроса на применение купона и подмена ответа сервера ошибкой 500."
        )
        logging.debug(
            "Перехват и блокировка запроса на применение купона и подмена ответа сервера ошибкой 500."
        )
        self.promocode.replace_response()

    @allure.story(
        "Вкладка «Оформление заказа»: добавление валидного промокода одним пользователем к двум заказам."
    )
    @allure.title("Проверка единоразового использования промокода 'GIVEMEHALYAVA'.")
    def test4_check_single_using_valid_promocode(self):

        logging.info("Открытие сайта.")
        self.my_account_page.open_page()

        logging.debug("Проверка, что открыт нужный сайт.")
        self.my_account_page.is_main_page()

        logging.info("Переход на вкладку «Мой аккаунт».")  # noqa
        logging.debug("Клик по вкладке «Мой аккаунт».")
        self.my_account_page.my_account_tab_click()

        logging.debug("Проверка, что отображается страница «Мой аккаунт».")
        self.my_account_page.is_my_account_page()

        logging.info("Переход в окно регистрации.")
        logging.debug("Нажать кнопку «Зарегистрироваться».")
        self.my_account_page.button_registration_click()

        logging.debug("Проверка, что отображается окно «Регистрация».")
        self.my_account_page.is_registration_window()

        logging.info("Заполнение формы регистрации валидными значениями.")
        logging.debug("Ввод валидного имени пользователя.")
        self.my_account_page.enter_login(self.valid_data.USER_NAME_4)

        logging.debug(
            "Проверка, что в поле 'Имя пользователя' отображается введенное значение."
        )
        self.my_account_page.check_login_in_input(self.valid_data.USER_NAME_4)

        logging.debug("Ввод валидного адреса электронной почты.")
        self.my_account_page.enter_email(self.valid_data.EMAIL_ADDRESS_4)

        logging.debug(
            "Проверка, что в поле 'Адрес почты' отображается введенное значение."
        )
        self.my_account_page.check_email_in_input(self.valid_data.EMAIL_ADDRESS_4)

        logging.debug("Ввод валидного пароля.")
        self.my_account_page.enter_password(self.valid_data.PASSWORD_4)

        logging.debug("Проверка, что в поле 'Пароль' отображается введенное значение.")
        self.my_account_page.check_password_in_input(self.valid_data.PASSWORD_4)

        logging.info("Отправка заполненной формы регистрации.")
        logging.debug("Нажать кнопку 'Зарегистрироваться'.")
        self.my_account_page.click_submit_button()

        logging.debug("Проверка, что отображается окно 'Регистрация завершена'.")
        self.my_account_page.is_registration_finished()

        logging.debug("Перейти на 'Главную' страницу сайта.")
        self.slider.main_page_click()

        logging.debug("Проверка, что отображается 'Главная' страница сайта.")
        self.my_account_page.is_main_page()

        logging.info("Создание первого заказа. Добавление первого товара в корзину.")
        logging.debug("Фокус на одном из товаров в слайдере.")  # noqa
        self.slider.focus_element_1()

        logging.debug("Ожидание появления кнопки 'В корзину'.")
        self.slider.button1_is_visible()

        logging.debug("Клик по кнопке 'В корзину'.")
        self.slider.button1_click()

        logging.debug(
            "Проверить, что сумма возле иконки тележки равна стоимости выбранного товара."
        )
        self.cart_icon.change_price_in_cart()

        logging.info("Переход на вкладку «Оформление заказа».")
        logging.debug("Клик по вкладке «Оформление заказа».")
        self.place_order_page.place_order_tab_click()

        logging.debug("Проверка, что отображается страница «Оформление заказа».")
        self.place_order_page.is_place_order_page()

        logging.info("Применение купона «GIVEMEHALYAVA».")  # noqa
        logging.debug("Клик по ссылке «Нажмите для ввода купона».")
        self.promocode.showcoupon_link_click()

        logging.debug("Ввод в поле применения купона «GIVEMEHALYAVA».")
        self.promocode.fill_coupon_field(self.valid_data.COUPON_NAME)

        logging.debug("Кликнуть по кнопке «Применить купон».")
        self.promocode.apply_coupon_button_click()

        logging.info("Проверка, что конечная сумма заказа уменьшилась на 10%.")
        logging.debug(
            "Проверить, что сумма скидки составляет 10% от общей суммы заказа."
        )
        self.promocode.is_discount_amount_10_percent()

        logging.debug(
            "Проверить, что итоговая сумма заказа уменьшилась на сумму скидки."
        )
        self.promocode.check_total_amount()

        logging.info(
            "Заполнение обязательных полей формы валидными значениями личных данных."
        )  # noqa
        logging.debug("Заполнить поле 'Имя' валидным значением.")
        self.place_order_page.check_name_in_name_field()

        logging.debug("Заполнить поле 'Фамилия' валидным значением.")
        self.place_order_page.check_last_name_in_last_name_field()

        logging.debug("Заполнить поле 'Адрес' валидным значением.")
        self.place_order_page.check_address_in_address_field()

        logging.debug("Заполнить поле 'Город / Населенный пункт' валидным значением.")
        self.place_order_page.check_city_in_city_field()

        logging.debug("Заполнить поле 'Область' валидным значением.")
        self.place_order_page.check_region_in_region_field()

        logging.debug("Заполнить поле 'Почтовый индекс' валидным значением.")
        self.place_order_page.check_postcode_in_postcode_field()

        logging.debug("Заполнить поле 'Телефон' валидным значением.")
        self.place_order_page.check_phone_in_phone_field()

        logging.info("Заполнение дополнительных полей формы.")
        logging.debug("Указать завтрашнюю дату в поле 'Дата заказа'.")
        self.place_order_page.choose_date_tomorrow()

        logging.debug(
            "Проверить, что завтрашняя дата отображается в поле 'Дата заказа'."
        )
        self.place_order_page.check_date_tomorrow()

        logging.info("Подтверждение согласия с условиями сайта.")
        logging.debug(
            "Кликнуть по чекбоксу, подтверждающему согласие с условиями сайта."
        )
        self.place_order_page.checkbox_terms_click()

        logging.debug(
            "Проверить, что чекбокс, подтверждающий согласие с условиями сайта, выбран."
        )
        self.place_order_page.checkbox_terms_is_selected()

        logging.info("Отправка заполненной формы.")
        logging.debug("Кликнуть по кнопке 'Оформить заказ'.")
        self.place_order_page.button_place_order_click()

        logging.info("Проверка получения заказа и соответствия суммы и личных данных.")
        logging.debug("Проверить, появилось ли подтверждение о получении заказа.")
        self.place_order_page.is_order_confirmed()

        logging.debug("Перейти на 'Главную' страницу сайта.")
        self.slider.main_page_click()

        logging.debug("Проверка, что отображается 'Главная' страница сайта.")
        self.my_account_page.is_main_page()

        logging.info("Создание второго заказа. Добавление второго товара в корзину.")
        logging.debug("Фокус на одном из товаров в слайдере.")  # noqa
        self.slider.focus_element_2()

        logging.debug("Ожидание появления кнопки 'В корзину'.")
        self.slider.button2_is_visible()

        logging.debug("Клик по кнопке 'В корзину'.")
        self.slider.button2_click()

        logging.debug(
            "Проверить, что сумма возле иконки тележки равна стоимости выбранного товара."
        )
        self.cart_icon.check_price_in_cart()

        logging.info("Переход на вкладку «Оформление заказа».")
        logging.debug("Клик по вкладке «Оформление заказа».")
        self.place_order_page.place_order_tab_click()

        logging.debug("Проверка, что отображается страница «Оформление заказа».")
        self.place_order_page.is_place_order_page()

        logging.info("Применение купона «GIVEMEHALYAVA» ко второму заказу.")
        logging.debug("Клик по ссылке «Нажмите для ввода купона».")
        self.promocode.showcoupon_link_click()

        logging.debug("Ввод в поле применения купона «GIVEMEHALYAVA».")
        self.promocode.fill_coupon_field(self.valid_data.COUPON_NAME)

        logging.debug("Кликнуть по кнопке «Применить купон».")
        self.promocode.apply_coupon_button_click()

        logging.info("Проверка, что валидный купон не был принят для второго заказа.")
        logging.debug(
            "Проверить, что сообщение об отказе применения купона не соответствует 'Coupon code applied "
            "successfully.'"
        )
        self.promocode.check_failure_coupon_alert()
