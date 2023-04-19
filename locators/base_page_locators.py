from selenium.webdriver.common.by import By


class BasePageLocators:
    # Логотип "Самоката" в хэдере
    HEADER_SCOOTER_LOGO = (By.XPATH, '//*[@href="/"]')
    # Логотип Яндекса в хэдере
    HEADER_YANDEX_LOGO = (By.XPATH, '//*[@href="//yandex.ru"]')
    # Кнопка "Заказать" в хэдере
    HEADER_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
