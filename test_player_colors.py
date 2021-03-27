from unittest import TestCase
from game import color_string_green


class TestColorStringGreen(TestCase):
    def test_color_string_green_correct_return(self):
        string = "Chris"
        expected = "\u001b[32;1mChris\u001b[0m"
        self.assertEqual(color_string_green(string), expected)

    def test_color_string_green_correct_type(self):
        string = "Chris"
        self.assertEqual(type(color_string_green(string)), str)