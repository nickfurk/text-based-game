from unittest import TestCase
from unittest.mock import patch
from game import player_name_generator


class TestPlayerNameGenerator(TestCase):

    @patch('builtins.input', return_value="Paula")
    def test_player_name_is_same_as_input(self, mock_input):
        actual = player_name_generator()
        expected_output = "Paula"
        self.assertEqual(actual, expected_output)

    @patch('builtins.input', return_value="apaul")
    def test_player_name_first_letter_becomes_capital(self, mock_input):
        actual = player_name_generator()
        expected_output = "Apaul"
        self.assertEqual(actual, expected_output)

    @patch('builtins.input', return_value="lirpa")
    def test_output_is_string(self, mock_input):
        actual = player_name_generator()
        expected_output = "Lirpa"
        self.assertEqual(type(actual), type(expected_output))