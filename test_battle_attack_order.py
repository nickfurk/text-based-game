from unittest import TestCase
from unittest.mock import patch
from game import battle_attack_order
import game
import io


class TestBattleAttackOrder(TestCase):
    @patch('game.roll_die', side_effect=[50, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_attack_order_print(self, mock_stdout, mock_die):
        expected_output = "Let's see who gets to attack first this round!\n\n"
        battle_attack_order()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('game.roll_die', side_effect=[50, 1])
    def test_battle_attack_order_player_first(self, mock_die):
        expected_output = True
        self.assertEqual(battle_attack_order(), expected_output)

    @patch('game.roll_die', side_effect=[1, 50])
    def test_battle_attack_order_monster_first(self, mock_die):
        expected_output = False
        self.assertEqual(battle_attack_order(), expected_output)

    @patch('game.roll_die', side_effect=[1, 1, 1, 50])
    def test_battle_attack_order_same_number(self, mock_die):
        expected_output = False
        self.assertEqual(battle_attack_order(), expected_output)
