import allure
from data.order_data import *
from pages.main_page import MainPage
from pages.order_page import *


class TestScooterOrder:

    @allure.description('Заказ самоката через кнопку "Заказать" в хэдере')
    def test_scooter_order_from_header_order_button(self, driver):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_base_page()
        main_page.accept_cookies()
        base_page.click_on_header_order_button()
        order_page.fill_order_form_1(UserMaleFirstForm.name_1,
                                     UserMaleFirstForm.last_name_1,
                                     UserMaleFirstForm.address_1,
                                     UserMaleFirstForm.metro_station_1,
                                     UserMaleFirstForm.phone)
        order_page.click_next_button_on_order_form_1()
        order_page.fill_order_form_2(UserMaleSecondForm.date_1,
                                     UserMaleSecondForm.rental_period_1,
                                     UserMaleSecondForm.scooter_finish_1,
                                     UserMaleSecondForm.comment_1)
        order_page.click_order_button_form_2()
        order_page.confirm_order_on_modal()
        modal = order_page.check_successful_order_message()
        expected_text = 'Заказ оформлен'
        order_page.check_presence_of_check_order_status_button()
        assert expected_text in modal, \
            f'Текст "{expected_text}" не обнаружен в модальном окне'

    @allure.description('Заказ самоката через кнопку "Заказать" на главной')
    def test_scooter_order_from_order_button(self, driver):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_base_page()
        main_page.accept_cookies()
        main_page.click_on_order_button()
        order_page.fill_order_form_1(UserFemaleFirstForm.name_2,
                                     UserFemaleFirstForm.last_name_2,
                                     UserFemaleFirstForm.address_2,
                                     UserFemaleFirstForm.metro_station_2,
                                     UserFemaleFirstForm.phone)
        order_page.click_next_button_on_order_form_1()
        order_page.fill_order_form_2(UserFemaleSecondForm.date_2,
                                     UserFemaleSecondForm.rental_period_2,
                                     UserFemaleSecondForm.scooter_finish_2,
                                     UserFemaleSecondForm.comment_2)
        order_page.click_order_button_form_2()
        order_page.confirm_order_on_modal()
        modal = order_page.check_successful_order_message()
        expected_text = 'Заказ оформлен'
        order_page.check_presence_of_check_order_status_button()
        assert expected_text in modal, \
            f'Текст "{expected_text}" не обнаружен в модальном окне'
