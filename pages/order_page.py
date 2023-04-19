import allure
from locators.order_page_locators import *
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем первую форму на странице оформления заказа')
    def fill_order_form_1(
            self, name, last_name, address, metro_station, phone):
        self.find_any_element(
            FirstOrderFormLocators.NAME_FIELD).send_keys(name)
        self.find_any_element(
            FirstOrderFormLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.find_any_element(
            FirstOrderFormLocators.ADDRESS_FIELD).send_keys(address)
        self.find_any_element(
            FirstOrderFormLocators.METRO_STATION_FIELD).send_keys(
            metro_station)
        self.find_any_element(
            FirstOrderFormLocators.CLICK_SUGGESTED_METRO_STATION).click()
        self.find_any_element(
            FirstOrderFormLocators.NUM_FIELD).send_keys(phone)

    @allure.step('После заполнения первой формы, кликаем на кнопку "Далее" '
                 'на странице оформления заказа')
    def click_next_button_on_order_form_1(self):
        self.find_any_element(FirstOrderFormLocators.NEXT_BUTTON).click()

    @allure.step('Заполняем вторую форму на странице оформления заказа')
    def fill_order_form_2(self, date, rental_period, scooter_finish, comment):
        self.find_any_element(
            SecondOrderFormLocators.DATE_FIELD).send_keys(date)
        self.find_any_element(
            SecondOrderFormLocators.CLICK_SELECTED_DATE).click()
        self.find_any_element(
            SecondOrderFormLocators.RENTAL_PERIOD_FIELD).click()
        self.driver.find_elements(
            *SecondOrderFormLocators.DROPDOWN_RENTAL_PERIOD)[
            rental_period].click()
        self.driver.find_elements(
            *SecondOrderFormLocators.SCOOTER_FINISH_CHECKBOXES)[
            scooter_finish].click()
        self.find_any_element(
            SecondOrderFormLocators.COMMENT).send_keys(comment)

    @allure.step('После заполнения второй формы, кликаем на кнопку "Заказать" '
                 'на странице оформления заказа')
    def click_order_button_form_2(self):
        self.find_any_element(SecondOrderFormLocators.ORDER_BUTTON).click()

    @allure.step('Подтверждаем оформление заказа в модальном окне')
    def confirm_order_on_modal(self):
        self.find_any_element(ModalWindowLocators.CONFIRM_BUTTON).click()

    @allure.step('В модальном окне, проверяем сообщение об успешном оформлении'
                 ' заказа')
    def check_successful_order_message(self):
        return self.find_any_element(ModalWindowLocators.ORDER_MODAL).text

    @allure.step('В модальном окне об успешном оформлении заказа, '
                 'проверяем наличие кнопки "Посмотреть статус"')
    def check_presence_of_check_order_status_button(self):
        self.find_any_element(
            ModalWindowLocators.CHECK_ORDER_STATUS_BUTTON).click()
