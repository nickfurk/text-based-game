from unittest import TestCase
from unittest.mock import patch
from game import player_name_generator
import io


class TestPlayerNameGenerator(TestCase):
    @patch('builtins.input', side_effect=["Paul"])
    @patch('game.random_name_generator', side_effect=["I would like to choose my own name!"])
    def test_player_name_generator_choose_own_name(self, mock_generate, mock_input):
        expected_output = "Paul"
        self.assertEqual(player_name_generator(), expected_output)

    @patch('game.random_name_generator', side_effect=["Stirring Lyrebird"])
    def test_player_name_generator_choose_name_given(self, mock_generate):
        expected_output = "Stirring Lyrebird"
        self.assertEqual(player_name_generator(), expected_output)

    @patch('game.random_name_generator', side_effect=["I would like to choose another one at random", "April"])
    def test_player_name_generator_choose_another_random(self, mock_generate):
        expected_output = "April"
        self.assertEqual(player_name_generator(), expected_output)

    @patch('game.random_name_generator', side_effect=["King Zelda"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_name_generator_correct_print(self, mock_stdout, mock_generator):
        expected_output = "\nWelcome to the game, \u001b[32;1mKing Zelda\u001b[0m.\n\n"
        player_name_generator()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
