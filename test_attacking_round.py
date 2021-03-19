from unittest import TestCase
from unittest.mock import patch
from game import attacking_round
import io


class TestAttackingRound(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_missed_attack(self, mock_output):
        player = {"name": "Leo"}
        monster = {"hp": 5}
        attacking_round(player, monster, 0)
        expected = "\nLeo has missed the attack!\n\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_damage_on_opponent(self, mock_output):
        player = {"name": "Leo"}
        monster = {"name": "Zelda", "hp": 10}
        attacking_round(player, monster, 5)
        expected = "Leo has done 5 damage to Zelda!\nZelda has 5 hp left!\n\n"
        self.assertEqual(mock_output.getvalue(), expected)

    def test_return_correct_opponent_dictionary(self):
        player = {"name": "Leo"}
        monster = {"name": "Zelda", "hp": 10}
        actual = attacking_round(player, monster, 5)
        expected = {"name": "Zelda", "hp": 5}
        self.assertEqual(actual, expected)
