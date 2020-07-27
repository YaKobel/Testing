import unittest
from full_name import full_name


class NameTestCase(unittest.TestCase):
    """Тесты для full_name.py"""

    def test_first_last_name(self):
        """ Имена вида 'Коб Ярослав' работают нормально?"""
        format_name = full_name('Коб', 'Ярослав')
        self.assertEqual(format_name, 'Коб Ярослав')


if __name__ == "__name__":
    unittest.main()

# __name__