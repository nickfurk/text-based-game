from unittest import TestCase
from unittest.mock import patch
from game import player_class_generator


class TestPlayerClassGenerator(TestCase):
    @patch('game.input_checker', side_effect=["Thief"])
    def test_player_class_generator_dictionary_class_gets_updated(self, mock_input):
        player_dictionary = {"class": ""}
        player_class_generator(player_dictionary)
        expected = {"class": "Thief"}
        self.assertEqual(player_dictionary, expected)

    @patch('builtins.input', side_effect=["1"])
    def test_player_class_generator_return_mage(self, mock_input):
        player_dictionary = {"class": ""}
        player_class_generator(player_dictionary)
        actual = player_dictionary["class"]
        expected = "Mage"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["2"])
    def test_player_class_generator_return_thief(self, mock_input):
        player_dictionary = {"class": ""}
        player_class_generator(player_dictionary)
        actual = player_dictionary["class"]
        expected = "Thief"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["3"])
    def test_player_class_generator_return_ranger(self, mock_input):
        player_dictionary = {"class": ""}
        player_class_generator(player_dictionary)
        actual = player_dictionary["class"]
        expected = "Ranger"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["4"])
    def test_player_class_generator_return_warrior(self, mock_input):
        player_dictionary = {"class": ""}
        player_class_generator(player_dictionary)
        actual = player_dictionary["class"]
        expected = "Warrior"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["2"])
    def test_player_class_generator_value_type(self, mock_input):
        player_dictionary = {"class": ""}
        player_class_generator(player_dictionary)
        self.assertEqual(type(player_dictionary["class"]), str)
