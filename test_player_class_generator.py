from unittest import TestCase
from unittest.mock import patch
from game import player_class_generator


class TestPlayerClassGenerator(TestCase):

    @patch('builtins.input', side_effect=["2"])
    def test_player_class_generator_dictionary_class_gets_updated(self, mock_input):
        player_dictionary = {"class": ""}
        player_class_generator(player_dictionary)
        actual = player_dictionary
        expected = {"class": "Thief"}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["2"])
    def test_player_class_generator_return_correct_class(self, mock_input):
        player_dictionary = {"class": ""}
        actual = player_class_generator(player_dictionary)
        expected = "Thief"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["4"])
    def test_player_class_generator_return_string(self, mock_input):
        player_dictionary = {"class": ""}
        actual = player_class_generator(player_dictionary)
        self.assertEqual(type(actual), str)
