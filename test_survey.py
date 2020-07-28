import unittest
from survey import AnonymousSurvey

class TestAnonmySurvey(unittest.TestCase):
    """Тесты для класов"""

    def test_store_single_response(self):
        """Проверяется, что один ответ сохранен в списке"""
        question = "Какой язык программирования вас найболее интересен?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Java')

        self.assertIn('Java', my_survey.responses)

if __name__ == '__name__':
    unittest.main()