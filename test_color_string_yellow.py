from unittest import TestCase
from game import color_string_yellow


class TestColorStringYellow(TestCase):
    def test_color_string_yellow_correct_return(self):
        string = "Apple"
        expected = "\u001b[33;1mApple\u001b[0m"
        self.assertEqual(color_string_yellow(string), expected)

    def test_color_string_yellow_correct_type(self):
        string = "Apple"
        self.assertEqual(type(color_string_yellow(string)), str)
