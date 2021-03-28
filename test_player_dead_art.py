from unittest import TestCase
from unittest.mock import patch
from game import player_dead_art
import io


class TestPlayerDeadArt(TestCase):
    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_dead_art_correct_print(self, mock_stdout, mock_input, mock_quit):
        expected_output = "\n\n\n" \
                          "  ___   _                     _ \n" \
                          " / _ \ | |__    _ __    ___  | |\n" \
                          "| | | || '_ \  | '_ \  / _ \ | |\n" \
                          "| |_| || | | | | | | || (_) ||_|\n" \
                          " \___/ |_| |_| |_| |_| \___/ (_)\n" \
                          "                                \n" \
                          "__   __               _                   _                   _  _ \n" \
                          "\ \ / /  ___   _   _ ( ) _ __   ___    __| |  ___   __ _   __| || |\n" \
                          " \ V /  / _ \ | | | ||/ | '__| / _ \  / _` | / _ \ / _` | / _` || |\n" \
                          "  | |  | (_) || |_| |   | |   |  __/ | (_| ||  __/| (_| || (_| ||_|\n" \
                          "  |_|   \___/  \__,_|   |_|    \___|  \__,_| \___| \__,_| \__,_|(_)\n" \
                          "                                                                   \n" \
                          " _____                                     _         _ \n" \
                          "|_   _| _ __  _   _    __ _   __ _   __ _ (_) _ __  | |\n" \
                          "  | |  | '__|| | | |  / _` | / _` | / _` || || '_ \ | |\n" \
                          "  | |  | |   | |_| | | (_| || (_| || (_| || || | | ||_|\n" \
                          "  |_|  |_|    \__, |  \__,_| \__, | \__,_||_||_| |_|(_)\n" \
                          "              |___/          |___/                     \n\n"
        player_dead_art()
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_dead_art_correct_type(self, mock_stdout, mock_input, mock_quit):
        player_dead_art()
        self.assertEqual(str, type(mock_stdout.getvalue()))
