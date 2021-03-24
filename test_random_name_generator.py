from unittest import TestCase
from unittest.mock import patch
from game import random_name_generator


class TestRandomNameGenerator(TestCase):

    @patch('builtins.input', side_effect=["2"])
    def test_select_choose_another_random_name(self, mock_input):
        actual = random_name_generator()
        expected = "I would like to choose another one at random"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["3"])
    def test_select_choose_own_name(self, mock_input):
        actual = random_name_generator()
        expected = "I would like to choose my own name!"
        self.assertEqual(actual, expected)
