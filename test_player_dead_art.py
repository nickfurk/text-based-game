from unittest import TestCase
from unittest.mock import patch
from game import player_dead_art
import io


class TestPlayerDeadArt(TestCase):
    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_dead_art_correct_print(self, mock_stdout, mock_input, mock_quit):
        expected_output = "\n\n\nASCII ART HERE\n"
        player_dead_art()
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_dead_art_correct_type(self, mock_stdout, mock_input, mock_quit):
        self.assertEqual(str, type(mock_stdout.getvalue()))
