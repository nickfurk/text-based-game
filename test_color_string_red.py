from unittest import TestCase
from game import color_string_red


class TestColorStringRed(TestCase):
    def test_color_string_red_correct_return(self):
        string = "Paul"
        expected = "\u001b[31mPaul\u001b[0m"
        self.assertEqual(color_string_red(string), expected)

    def test_color_string_red_correct_type(self):
        string = "Paul"
        self.assertEqual(type(color_string_red(string)), str)
