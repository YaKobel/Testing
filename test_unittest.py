import unittest
from full_name import full_name


class NameTestCase(unittest.TestCase):
    """Тесты для full_name.py"""

    def test_first_last_name(self):
        """ Имена вида 'Коб Ярослав' работают нормально?"""
        format_name = full_name('Коб', 'Ярослав')
        self.assertEqual(format_name, 'Коб Ярослав')

    def test_first_last_middle(self):
        """ Имена вида 'Коб Ярослав Анатольевич' работают нормально?"""
        format_name = full_name('Коб', 'Ярослав', 'Анатолиевич')
        self.assertEqual(format_name, 'Коб Ярослав Анатолиевич')


if __name__ == "__name__":
    unittest.main()
