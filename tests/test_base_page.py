import allure
from pages.main_page import MainPage, BasePage


class TestHeaderLogos:

    @allure.description('Клик на лого "Самокат" в хэдере — редирект на главную'
                        ' страницу Самоката (кликаем со страницы заказа)')
    def test_click_scooter_logo_from_order_page(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_base_page()
        main_page.accept_cookies()
        main_page.click_on_order_button()
        base_page.go_to_scooter_main_page_from_scooter_logo()
        expected_url = 'https://qa-scooter.praktikum-services.ru/'
        assert driver.current_url == expected_url, \
            f'{driver.current_url} не соответствует {expected_url}'

    @allure.description('Клик на лого Яндекса в хэдере — в новой вкладке '
                        'открывается yandex.ru с редиректом на Дзен '
                        '(кликаем со страницы заказа)')
    def test_click_yandex_logo_from_order_page(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_base_page()
        main_page.accept_cookies()
        base_page.click_on_header_order_button()
        base_page.go_to_yandex_page_from_yandex_logo()
        expected_url = 'https://dzen.ru/?yredirect=true'
        assert driver.current_url == expected_url, \
            f'{driver.current_url} не соответствует {expected_url}'
