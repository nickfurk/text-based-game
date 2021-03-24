from unittest import TestCase
from unittest.mock import patch
from game import player_name_generator
import io


class TestPlayerNameGenerator(TestCase):
    @patch('builtins.input', side_effect=["I would like to choose another one at random"])
    @patch('game.random_name_generator', side_effect=["Stirring Lyrebird", "Glossy Outstanding Collie Of Politeness"])
    def test_player_name_generator_choice_from_list(self, mock_generate, mock_input):
        actual = player_name_generator()
        expected_output = "Glossy Outstanding Collie Of Politeness"
        self.assertEqual(actual, expected_output)

    @patch('builtins.input', side_effect=["5", "Paul"])
    def test_player_name_generator_player_chooses(self, mock_input):
        actual = player_name_generator()
        expected_output = "Paul"
        self.assertEqual(actual, expected_output)

    @patch('builtins.input', side_effect=["5", "apaul"])
    def test_player_name_generator_first_letter_becomes_capital(self, mock_input):
        actual = player_name_generator()
        expected_output = "Apaul"
        self.assertEqual(actual, expected_output)

    @patch('builtins.input', side_effect=["5", "lirpa"])
    def test_player_name_generator_output_is_string(self, mock_input):
        actual = player_name_generator()
        expected_output = "Lirpa"
        self.assertEqual(type(actual), type(expected_output))

    @patch('builtins.input', side_effect=["5", "lirpa"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_name_generator_correct_print(self, mock_stdout, mock_input):
        player_name_generator()
        expected_output = "Please choose one of the provided names, or your own.\n" \
                          "{'1': 'Paul'\n" \
                          " '2': 'April'\n" \
                          " '3': 'Leo'\n" \
                          " '4': 'Michelle'\n" \
                          " '5': 'Choose my own'}\n\n" \
                          "Welcome to the game, Lirpa.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
