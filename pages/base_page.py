import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Открываем главную страницу Яндекс Самокат')
    def go_to_base_page(self):
        self.driver.get(self.base_url)

    @allure.step('Кликаем на кнопку "Заказать" в хэдере')
    def click_on_header_order_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                BasePageLocators.HEADER_ORDER_BUTTON)).click()

    @allure.step('Ищем элемент')
    def find_any_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Переход на главную страницу Яндекс Самокат')
    def go_to_scooter_main_page_from_scooter_logo(self):
        return self.find_any_element(
            BasePageLocators.HEADER_SCOOTER_LOGO).click()

    @allure.step('Переход на yandex.ru c редиректом на Дзен')
    def go_to_yandex_page_from_yandex_logo(self):
        self.find_any_element(BasePageLocators.HEADER_YANDEX_LOGO).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, 5).until(
            EC.url_to_be('https://dzen.ru/?yredirect=true'))
