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

    def test_five_responses(self):
        """Проверяет что 5 ответов были сохраненны"""
        self.my_survey.store_response(self.responses[0:])
        self.assertIn(self.responses[0:], self.my_survey.responses)

    def test_three_responses(self):
        """Проверяет что 3 ответов были сохраненны"""
        self.my_survey.store_response(self.responses[2:4])
        self.assertIn(self.responses[2:4], self.my_survey.responses)


if __name__ == '__name__':
    unittest.main()