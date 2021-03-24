from unittest import TestCase
from unittest.mock import patch
from game import game_over
import io


class TestGameOver(TestCase):
    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_correct_print(self, mock_stdout, mock_input, mock_quit):
        expected_output = "\n\n\nThanks for playing! The game is over, goodbye!\n"
        game_over()
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_correct_type(self, mock_stdout, mock_input, mock_quit):
        game_over()
        self.assertEqual(str, type(mock_stdout.getvalue()))
