from unittest import TestCase
from game import underline_string


class TestUnderlineString(TestCase):
    def test_underline_string_correct_return(self):
        string = "April"
        expected = "\033[4mApril\u001b[0m"
        self.assertEqual(underline_string(string), expected)

    def test_underline_string_correct_type(self):
        string = "April"
        self.assertEqual(type(underline_string(string)), str)
