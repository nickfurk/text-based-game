from unittest import TestCase
from unittest.mock import patch
from game import attacking_round
import io


class TestAttackingRound(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attacking_round_missed_attack(self, mock_output):
        player = {"name": "Leo", "category": "player", 'class_dictionary': {'attack_name': 'Pet the head'}}
        monster = {"hp": 5, "category": "monster", 'attack_name': 'Scratch'}
        attacking_round(player, monster, 0)
        expected = "\nLeo has missed the attack!\n\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attacking_round_damage_on_opponent(self, mock_output):
        player = {"name": "Leo", "category": "player", 'class_dictionary': {'attack_name': 'Pet the head'}}
        monster = {"name": "Zelda", "hp": 10, "category": "monster", 'attack_name': 'Scratch'}
        attacking_round(player, monster, 5)
        expected = "Leo has used Pet the head and has done 5 damage to Zelda!\n" \
                   "Zelda has 5 hp left!\n\n"
        self.assertEqual(mock_output.getvalue(), expected)

    def test_attacking_round_return_correct_opponent_dictionary(self):
        player = {"name": "Leo", "category": "player", 'class_dictionary': {'attack_name': 'Pet the head'}}
        monster = {"name": "Zelda", "hp": 10, "category": "monster", 'attack_name': 'Scratch'}
        attacking_round(player, monster, 5)
        expected = {"name": "Zelda", "hp": 5, "category": "monster", 'attack_name': 'Scratch'}
        self.assertEqual(monster, expected)
