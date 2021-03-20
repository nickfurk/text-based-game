from unittest import TestCase
from unittest.mock import patch
from game import display_map
from colorama import Fore, Style
import io


class TestDisplayMap(TestCase):

    @patch('game.BOARD_SIZE', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_correct_map(self, mock_output, mock_board):
        player_info = {"position": [0, 0]}
        boss_info = {"position": [2, 2]}
        display_map(player_info, boss_info)
        expected = Fore.GREEN + '[X]' + Style.RESET_ALL + '[ ][ ][ ]\n[ ][ ][ ][ ]\n[ ][ ]' + Fore.RED + '[#]' \
            + Style.RESET_ALL + '[ ]\n[ ][ ][ ][ ]\n'
        self.assertEqual((mock_output.getvalue()), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_string(self, mock_output):
        player_info = {"position": [0, 0]}
        boss_info = {"position": [2, 2]}
        display_map(player_info, boss_info)
        self.assertEqual(type(mock_output.getvalue()), str)
