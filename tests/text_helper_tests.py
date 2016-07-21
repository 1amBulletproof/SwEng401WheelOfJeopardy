import unittest

from wheelofjeopardy.text_helper import apostrophize, pluralize

class TestApostrophize(unittest.TestCase):
    def test_name_ends_with_s(self):
        self.assertEqual("James'", apostrophize('James'))

    def test_name_does_not_end_with_s(self):
        self.assertEqual("Arthur's", apostrophize('Arthur'))

class TestPluralize(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(
            'shrubberies', pluralize(0, 'shrubbery', 'shrubberies')
        )

    def test_one(self):
        self.assertEqual(
            'shrubbery', pluralize(1, 'shrubbery', 'shrubberies')
        )

    def test_other(self):
        self.assertEqual(
            'shrubberies', pluralize(0, 'shrubbery', 'shrubberies')
        )
