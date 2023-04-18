import allure
import pytest
from data.important_questions_data import ImportantQuestionsData
from pages.base_page import BasePage


class TestImportantQuestions:

    @allure.description('Проверка раздела "Вопросы о важном"')
    @pytest.mark.parametrize('question, answer, get_answer',
                             ImportantQuestionsData.question_and_answers)
    def test_get_answer_to_question(
            self, driver, question, answer, get_answer):
        get = BasePage(driver)
        get.go_to_base_page_and_accept_cookies()
        get.click_question(question)
        get.get_answer(answer)
        answer = get.get_answer(answer)
        assert answer == get_answer, \
            f'Текст ответа не соответствует ожидаемому'
