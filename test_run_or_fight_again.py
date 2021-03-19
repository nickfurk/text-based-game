from unittest import TestCase
from unittest.mock import patch
from game import run_or_fight_again
import game
import io

class TestRunOrFightAgain(TestCase):
    @patch('game.input_checker', return_value='Yes')
    def test_run_or_fight_again_yes(self, mock_input):
        expected_output = 'Yes'
        self.assertEqual(expected_output, run_or_fight_again())

    @patch('game.input_checker', return_value='No')
    def test_run_or_fight_again_no(self, mock_input):
        expected_output = 'No'
        self.assertEqual(expected_output, run_or_fight_again())

    @patch('game.input_checker', side_effect=['', 'Yes'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_or_fight_again_error(self, mock_stdout, mock_input):
        monster = {'name': 'Paul'}
        expected_output = '\nWould you like to keep fighting?\n\n' \
                          ' is not a valid choice!, Please choose again: \n'
        run_or_fight_again()
        self.assertEqual(expected_output, mock_stdout.getvalue())
