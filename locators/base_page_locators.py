from selenium.webdriver.common.by import By


class BasePageLocators:
    # Логотип "Самоката" в хэдере
    HEADER_SCOOTER_LOGO = (By.XPATH, '//*[@href="/"]')
    # Логотип Яндекса в хэдере
    HEADER_YANDEX_LOGO = (By.XPATH, '//*[@href="//yandex.ru"]')
    # Кнопка согласия с использованием куки
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    # Кнопка "Заказать" в хэдере
    HEADER_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    # Кнопка "Заказать"
    ORDER_BUTTON = \
        (By.XPATH,
         '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    # Вопрос 1
    QUESTION_1 = (By.ID, 'accordion__heading-0')
    # Ответ на вопрос 1
    ANSWER_1 = (By.ID, 'accordion__panel-0')
    # Вопрос 2
    QUESTION_2 = (By.ID, 'accordion__heading-1')
    # Ответ на вопрос 2
    ANSWER_2 = (By.ID, 'accordion__panel-1')
    # Вопрос 3
    QUESTION_3 = (By.ID, 'accordion__heading-2')
    # Ответ на вопрос 3
    ANSWER_3 = (By.ID, 'accordion__panel-2')
    # Вопрос 4
    QUESTION_4 = (By.ID, 'accordion__heading-3')
    # Ответ на вопрос 4
    ANSWER_4 = (By.ID, 'accordion__panel-3')
    # Вопрос 5
    QUESTION_5 = (By.ID, 'accordion__heading-4')
    # Ответ на вопрос 5
    ANSWER_5 = (By.ID, 'accordion__panel-4')
    # Вопрос 6
    QUESTION_6 = (By.ID, 'accordion__heading-5')
    # Ответ на вопрос 6
    ANSWER_6 = (By.ID, 'accordion__panel-5')
    # Вопрос 7
    QUESTION_7 = (By.ID, 'accordion__heading-6')
    # Ответ на вопрос 7
    ANSWER_7 = (By.ID, 'accordion__panel-6')
    # Вопрос 8
    QUESTION_8 = (By.ID, 'accordion__heading-7')
    # Ответ на вопрос 8
    ANSWER_8 = (By.ID, 'accordion__panel-7')
