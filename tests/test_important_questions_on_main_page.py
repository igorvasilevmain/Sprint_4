import allure
import pytest
from data.important_questions_data import ImportantQuestionsData
from pages.main_page import MainPage, BasePage


class TestImportantQuestions:

    @allure.description('Проверка раздела "Вопросы о важном"')
    @pytest.mark.parametrize('question, answer, get_answer',
                             ImportantQuestionsData.question_and_answers)
    def test_get_answer_to_question(
            self, driver, question, answer, get_answer):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_base_page()
        main_page.accept_cookies()
        main_page.click_question(question)
        main_page.get_answer(answer)
        answer = main_page.get_answer(answer)
        assert answer == get_answer, \
            f'Текст ответа не соответствует ожидаемому'
