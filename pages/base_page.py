import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Открываем главную страницу Яндекс Самокат и принимаем куки')
    def go_to_base_page_and_accept_cookies(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                BasePageLocators.COOKIE_BUTTON)).click()

    @allure.step('Кликаем на кнопку "Заказать" в хэдере')
    def click_on_header_order_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                BasePageLocators.HEADER_ORDER_BUTTON)).click()

    @allure.step('Кликаем на кнопку "Заказать" на главной')
    def click_on_order_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                BasePageLocators.ORDER_BUTTON)).click()

    @allure.step('Ищем элемент')
    def find_any_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Кликаем на вопрос в разделе "Вопросы о важном"')
    def click_question(self, question):
        question = self.find_any_element(question)
        self.driver.execute_script("arguments[0].click();", question)

    @allure.step('Получаем текст ответа в разделе "Вопросы о важном"')
    def get_answer(self, answer):
        return self.find_any_element(answer).text
