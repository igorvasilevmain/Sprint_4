import allure
from data.order_data import *
from pages.order_page import *


class TestScooterOrder:

    @allure.description('Заказ самоката через кнопку "Заказать" в хэдере')
    def test_scooter_order_from_header_order_button(self, driver):
        order = OrderPage(driver)
        order.go_to_base_page_and_accept_cookies()
        order.click_on_header_order_button()
        order.fill_order_form_1(
            name=UserMale.name_1,
            last_name=UserMale.last_name_1,
            address=UserMale.address_1,
            metro_station=UserMale.metro_station_1,
            phone=UserMale.phone)
        order.click_next_button_on_order_form_1()
        order.fill_order_form_2(
            date=UserMale.date_1,
            rental_period=UserMale.rental_period_1,
            scooter_finish=UserMale.scooter_finish_1,
            comment=UserMale.comment_1)
        order.click_order_button_form_2()
        order.confirm_order_on_modal()
        modal = order.check_successful_order_message()
        expected_text = 'Заказ оформлен'
        order.check_presence_of_check_order_status_button()
        assert expected_text in modal, \
            f'Текст "{expected_text}" не обнаружен в модальном окне'

    @allure.description('Заказ самоката через кнопку "Заказать" на главной')
    def test_scooter_order_from_order_button(self, driver):
        order = OrderPage(driver)
        order.go_to_base_page_and_accept_cookies()
        order.click_on_order_button()
        order.fill_order_form_1(
            name=UserFemale.name_2,
            last_name=UserFemale.last_name_2,
            address=UserFemale.address_2,
            metro_station=UserFemale.metro_station_2,
            phone=UserFemale.phone)
        order.click_next_button_on_order_form_1()
        order.fill_order_form_2(
            date=UserFemale.date_2,
            rental_period=UserFemale.rental_period_2,
            scooter_finish=UserFemale.scooter_finish_2,
            comment=UserFemale.comment_2)
        order.click_order_button_form_2()
        order.confirm_order_on_modal()
        modal = order.check_successful_order_message()
        expected_text = 'Заказ оформлен'
        order.check_presence_of_check_order_status_button()
        assert expected_text in modal, \
            f'Текст "{expected_text}" не обнаружен в модальном окне'


class TestHeaderLogos:

    @allure.description('Клик на лого "Самокат" в хэдере — редирект на главную'
                        ' страницу Самоката (кликаем со страницы заказа)')
    def test_click_scooter_logo_from_order_page(self, driver):
        click = OrderPage(driver)
        click.go_to_base_page_and_accept_cookies()
        click.click_on_order_button()
        click.go_to_scooter_base_page_from_scooter_logo()
        expected_url = 'https://qa-scooter.praktikum-services.ru/'
        assert driver.current_url == expected_url, \
            f'{driver.current_url} не соответствует {expected_url}'

    @allure.description('Клик на лого Яндекса в хэдере — в новой вкладке '
                        'открывается yandex.ru с редиректом на Дзен '
                        '(кликаем со страницы заказа)')
    def test_click_yandex_logo_from_order_page(self, driver):
        click = OrderPage(driver)
        click.go_to_base_page_and_accept_cookies()
        click.click_on_header_order_button()
        click.go_to_yandex_page_from_yandex_logo()
        expected_url = 'https://dzen.ru/?yredirect=true'
        assert driver.current_url == expected_url, \
            f'{driver.current_url} не соответствует {expected_url}'
