from unittest import TestCase
from unittest.mock import patch
from game import game_win_art
import io


class TestGameWinArt(TestCase):
    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_win_art_correct_print(self, mock_stdout, mock_input, mock_quit):
        expected_output = "\n\n\n" \
                          "  ____                                    _         _ \n" \
                          " / ___|  ___   _ __    __ _  _ __   __ _ | |_  ___ | |\n" \
                          "| |     / _ \ | '_ \  / _` || '__| / _` || __|/ __|| |\n" \
                          "| |___ | (_) || | | || (_| || |   | (_| || |_ \__ \|_|\n" \
                          " \____| \___/ |_| |_| \__, ||_|    \__,_| \__||___/(_)\n" \
                          "                      |___/                           "\
                          "\n__   __               _                                        _ \n" \
                          "\ \ / /  ___   _   _ ( )__   __  ___  __      __  ___   _ __  | |\n" \
                          " \ V /  / _ \ | | | ||/ \ \ / / / _ \ \ \ /\ / / / _ \ | '_ \ | |\n" \
                          "  | |  | (_) || |_| |    \ V / |  __/  \ V  V / | (_) || | | ||_|\n" \
                          "  |_|   \___/  \__,_|     \_/   \___|   \_/\_/   \___/ |_| |_|(_)\n" \
                          "                                                                 \n\n"
        game_win_art()
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_win_art_correct_type(self, mock_stdout, mock_input, mock_quit):
        self.assertEqual(str, type(mock_stdout.getvalue()))
