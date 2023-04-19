import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Принимаем куки на главной странице')
    def accept_cookies(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.COOKIE_BUTTON)).click()

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_on_order_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_BUTTON)).click()

    @allure.step('Кликаем на вопрос в разделе "Вопросы о важном"')
    def click_question(self, question):
        question = self.find_any_element(question)
        return self.driver.execute_script("arguments[0].click();", question)

    @allure.step('Получаем текст ответа в разделе "Вопросы о важном"')
    def get_answer(self, answer):
        return self.find_any_element(answer).text
