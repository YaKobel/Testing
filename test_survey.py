import unittest
from survey import AnonymousSurvey

class TestAnonmySurvey(unittest.TestCase):
    """Тесты для класов AnonymousSurvey"""

    def setUp(self):
        """Создание опроса и набора ответов для всех методов"""
        question = "Какой язык программирования вас найболее интересен?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Java', 'Python', 'C#', 'Go', 'JavaScript']

    def test_store_single_response(self):
        """Проверяется, что один ответ сохранен в правильно"""
        self.my_survey.store_response(self.responses[1])
        self.assertIn(self.responses[1], self.my_survey.responses)


    # def test_five_responses(self):
    #     """Проверяет что 5 ответов были сохраненны"""
    #
    #     question = "Какой язык программирования вам по душе?"
    #     my_survey = AnonymousSurvey(question)
    #     responses5 = ['Java', 'Python', 'C#', 'Go', 'JavaScript']
    #     for response in responses5:
    #         my_survey.store_response(response)
    #
    #     for response in responses5:
    #         self.assertIn(response, my_survey.responses)

if __name__ == '__name__':
    unittest.main()