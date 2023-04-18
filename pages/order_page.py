import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем первую форму на странице оформления заказа')
    def fill_order_form_1(
            self, name, last_name, address, metro_station, phone):
        self.find_any_element(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find_any_element(
            OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.find_any_element(
            OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        self.find_any_element(
            OrderPageLocators.METRO_STATION_FIELD).send_keys(metro_station)
        self.find_any_element(
            OrderPageLocators.CLICK_SUGGESTED_METRO_STATION).click()
        self.find_any_element(OrderPageLocators.NUM_FIELD).send_keys(phone)

    @allure.step('После заполнения первой формы, кликаем на кнопку "Далее" '
                 'на странице оформления заказа')
    def click_next_button_on_order_form_1(self):
        self.find_any_element(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполняем вторую форму на странице оформления заказа')
    def fill_order_form_2(self, date, rental_period, scooter_finish, comment):
        self.find_any_element(OrderPageLocators.DATE_FIELD).send_keys(date)
        self.find_any_element(OrderPageLocators.CLICK_SELECTED_DATE).click()
        self.find_any_element(OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.driver.find_elements(
            *OrderPageLocators.DROPDOWN_RENTAL_PERIOD)[rental_period].click()
        self.driver.find_elements(
            *OrderPageLocators.SCOOTER_FINISH_CHECKBOXES)[
            scooter_finish].click()
        self.find_any_element(OrderPageLocators.COMMENT).send_keys(comment)

    @allure.step('После заполнения второй формы, кликаем на кнопку "Заказать" '
                 'на странице оформления заказа')
    def click_order_button_form_2(self):
        self.find_any_element(OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Подтверждаем оформление заказа в модальном окне')
    def confirm_order_on_modal(self):
        self.find_any_element(OrderPageLocators.CONFIRM_BUTTON).click()

    @allure.step('В модальном окне, проверяем сообщение об успешном оформлении'
                 ' заказа')
    def check_successful_order_message(self):
        return self.find_any_element(OrderPageLocators.ORDER_MODAL).text

    @allure.step('В модальном окне об успешном оформлении заказа, '
                 'проверяем наличие кнопки "Посмотреть статус"')
    def check_presence_of_check_order_status_button(self):
        self.find_any_element(
            OrderPageLocators.CHECK_ORDER_STATUS_BUTTON).click()

    @allure.step('Переход на главную страницу Яндекс Самокат')
    def go_to_scooter_base_page_from_scooter_logo(self):
        self.find_any_element(BasePageLocators.HEADER_SCOOTER_LOGO).click()

    @allure.step('Переход на yandex.ru c редиректом на Дзен')
    def go_to_yandex_page_from_yandex_logo(self):
        self.find_any_element(BasePageLocators.HEADER_YANDEX_LOGO).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(
            EC.url_to_be('https://dzen.ru/?yredirect=true'))
