from unittest import TestCase
from unittest.mock import patch
from game import game_over
import io


class TestGameOver(TestCase):
    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_correct_print(self, mock_stdout, mock_input, mock_quit):
        expected_output = "\n\n\n" \
                          " _____  _                    _            __                       _                _                _ \n" \
                          "|_   _|| |__    __ _  _ __  | | __ ___   / _|  ___   _ __   _ __  | |  __ _  _   _ (_) _ __    __ _ | |\n" \
                          "  | |  | '_ \  / _` || '_ \ | |/ // __| | |_  / _ \ | '__| | '_ \ | | / _` || | | || || '_ \  / _` || |\n" \
                          "  | |  | | | || (_| || | | ||   < \__ \ |  _|| (_) || |    | |_) || || (_| || |_| || || | | || (_| ||_|\n" \
                          "  |_|  |_| |_| \__,_||_| |_||_|\_\|___/ |_|   \___/ |_|    | .__/ |_| \__,_| \__, ||_||_| |_| \__, |(_)\n" \
                          "                                                           |_|               |___/            |___/    \n" \
                          " ____                                                         _     _    _                   _ \n" \
                          "/ ___|   ___   ___   _   _   ___   _   _   _ __    ___ __  __| |_  | |_ (_) _ __ ___    ___ | |\n" \
                          "\___ \  / _ \ / _ \ | | | | / _ \ | | | | | '_ \  / _ \\ \/ /| __| | __|| || '_ ` _ \  / _ \| |\n" \
                          " ___) ||  __/|  __/ | |_| || (_) || |_| | | | | ||  __/ >  < | |_  | |_ | || | | | | ||  __/|_|\n" \
                          "|____/  \___| \___|  \__, | \___/  \__,_| |_| |_| \___|/_/\_\ \__|  \__||_||_| |_| |_| \___|(_)\n" \
                          "                     |___/                                                                     "
        game_over()
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.quit', side_effect=[None])
    @patch('builtins.input', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over_correct_type(self, mock_stdout, mock_input, mock_quit):
        game_over()
        self.assertEqual(str, type(mock_stdout.getvalue()))
