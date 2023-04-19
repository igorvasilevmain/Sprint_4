from selenium.webdriver.common.by import By


class FirstOrderFormLocators:
    # Поле ввода имени
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    # Поле ввода фамилии
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    # Поле ввода адреса
    ADDRESS_FIELD = (By.XPATH,
                     '//input[@placeholder="* Адрес: куда привезти заказ"]')
    # Поле ввода станции метро
    METRO_STATION_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    # Клик на выбранную станцию
    CLICK_SUGGESTED_METRO_STATION = (By.CLASS_NAME, 'select-search__select')
    # Поле ввода номера телефона
    NUM_FIELD = (By.XPATH,
                 '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')


class SecondOrderFormLocators:
    # Поле ввода даты
    DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    # Клик на выбранную дату
    CLICK_SELECTED_DATE = (By.CLASS_NAME, 'react-datepicker__day--selected')
    # Поле выбора срока аренды
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')
    # Выпадающий список с выбором срока аренды
    DROPDOWN_RENTAL_PERIOD = (By.XPATH, '//*[@class="Dropdown-menu"]/div')
    # Список с цветами самоката
    SCOOTER_FINISH_CHECKBOXES = (By.XPATH,
                                 '//*[@class="Checkbox_Input__14A2w"]')
    # Поле ввода комментария
    COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    # Кнопка "Заказать"
    ORDER_BUTTON = \
        (By.XPATH,
         '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')


class ModalWindowLocators:
    # Кнопка подтверждения заказа
    CONFIRM_BUTTON = (By.XPATH,
                      '//button[@class="Button_Button__ra12g '
                      'Button_Middle__1CSJM" and (text()="Да")]')
    # Модальное окно подтверждения заказа / модальное окно успешно
    # оформленного заказа
    ORDER_MODAL = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    # Кнопка "Посмотреть статус"
    CHECK_ORDER_STATUS_BUTTON = (By.XPATH,
                                 '//button[text()="Посмотреть статус"]')
