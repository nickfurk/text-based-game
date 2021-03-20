from unittest import TestCase
from unittest.mock import patch
from game import fight_or_run_decision_boss_round
import game
import io


class TestFightOrRunDecisionBossRound(TestCase):
    @patch('game.input_checker', return_value='Yes')
    def test_fight_or_run_decision_boss_round_yes(self, mock_input):
        boss = {'name': 'Lord Zelda', 'hp': 30, 'damage': 15, 'position': [2, 3]}
        expected_output = 'Yes'
        self.assertEqual(expected_output, fight_or_run_decision_boss_round(boss))

    @patch('game.input_checker', return_value='No')
    def test_fight_or_run_decision_boss_round_no(self, mock_input):
        boss = {'name': 'Lord Zelda', 'hp': 30, 'damage': 15, 'position': [2, 3]}
        expected_output = 'No'
        self.assertEqual(expected_output, fight_or_run_decision_boss_round(boss))

    @patch('game.input_checker', return_value='Yes')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_decision_boss_round_correct_print(self, mock_stdout, mock_input):
        boss = {'name': 'Lord Zelda', 'hp': 30, 'damage': 15, 'position': [2, 3]}
        expected_output = "\nYou have encountered Lord Zelda!\nThe boss hp is 30, and the damage is 15.\n" \
                          "If you beat him, you will finish the game with a victory, if you fail however, the game " \
                          "will be finished.\nYou can choose to run away anytime you'd like and come back when you " \
                          "believe you are ready to defeat the boss!\n\n" \
                          "\nWould you like to fight?\n(We recommend going up against the boss at level 3, as you " \
                          "will have higher chances of winning)\n"
        fight_or_run_decision_boss_round(boss)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.input_checker', side_effect=['', 'No'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_decision_boss_round_error(self, mock_stdout, mock_input):
        boss = {'name': 'Lord Zelda', 'hp': 30, 'damage': 15, 'position': [2, 3]}
        expected_output = "\nYou have encountered Lord Zelda!\nThe boss hp is 30, and the damage is 15.\n" \
                          "If you beat him, you will finish the game with a victory, if you fail however, the game " \
                          "will be finished.\nYou can choose to run away anytime you'd like and come back when you " \
                          "believe you are ready to defeat the boss!\n\n" \
                          "\nWould you like to fight?\n(We recommend going up against the boss at level 3, as you " \
                          "will have higher chances of winning)\n" \
                          " is not a valid choice!, Please choose again: \n"
        fight_or_run_decision_boss_round(boss)
        self.assertEqual(expected_output, mock_stdout.getvalue())
