from unittest import TestCase
from unittest.mock import patch
from game import run_away_monster
import game
import io


class TestRunAwayMonster(TestCase):
    def test_run_away_monster_no_hp_monster(self):
        player = {"hp": 10}
        monster = {"name": "Zelda", "hp": 0}
        expected_output = False
        self.assertEqual(run_away_monster(monster, player), expected_output)

    def test_run_away_monster_no_hp_player(self):
        player = {"hp": 0}
        monster = {"name": "Zelda", "hp": 4}
        expected_output = False
        self.assertEqual(run_away_monster(monster, player), expected_output)

    @patch('game.roll_die', return_value=1)
    @patch('game.press_enter_to_continue', return_value='')
    def test_run_away_monster_success_bool_return(self, mock_continue, mock_die):
        player = {"hp": 3}
        monster = {"name": "Zelda", "hp": 2}
        expected_output = True
        self.assertEqual(run_away_monster(monster, player), expected_output)

    @patch('game.roll_die', return_value=1)
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_monster_success(self, mock_stdout, mock_continue, mock_die):
        player = {"hp": 3}
        monster = {"name": "Zelda", "hp": 2}
        expected_output = 'Zelda ran away!\n'
        run_away_monster(monster, player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('game.roll_die', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_monster_failure(self, mock_stdout, mock_die):
        player = {"hp": 3}
        monster = {"name": "Zelda", "hp": 2}
        expected_output = ''
        run_away_monster(monster, player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
