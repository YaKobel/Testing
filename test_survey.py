import unittest
from survey import AnonymousSurvey

class TestAnonmySurvey(unittest.TestCase):
    """Тесты для класов AnonymousSurvey"""

    def test_store_single_response(self):
        """Проверяется, что один ответ сохранен в списке"""
        question = "Какой язык программирования вас найболее интересен?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Java')

        self.assertIn('Java', my_survey.responses)

    def test_five_responses(self):
        """Проверяет что 5 ответов были сохраненны"""

        question = "Какой язык программирования вам по душе?"
        my_survey = AnonymousSurvey(question)
        responses5 = ['Java', 'Python', 'C#', 'Go', 'JavaScript']
        for response in responses5:
            my_survey.store_response(response)

        for response in responses5:
            self.assertIn(response, my_survey.responses)

if __name__ == '__name__':
    unittest.main()