from unittest import TestCase
from unittest.mock import patch
from game import fight_or_run_decision
import game
import io


class TestFightOrRunDecision(TestCase):
    @patch('game.input_checker', return_value='Yes')
    def test_fight_or_run_decision_yes(self, mock_input):
        monster = {'name': 'Paul'}
        expected_output = 'Yes'
        self.assertEqual(expected_output, fight_or_run_decision(monster))

    @patch('game.input_checker', return_value='No')
    def test_fight_or_run_decision_no(self, mock_input):
        monster = {'name': 'Paul'}
        expected_output = 'No'
        self.assertEqual(expected_output, fight_or_run_decision(monster))

    @patch('game.input_checker', return_value='Yes')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_decision_correct_print(self, mock_stdout, mock_input):
        monster = {'name': 'Paul'}
        expected_output = '\nYou have encountered Paul! Would you like to fight?\n\n'
        fight_or_run_decision(monster)
        self.assertEqual(expected_output, mock_stdout.getvalue())
