from unittest import TestCase
from unittest.mock import patch
from game import make_boss
import game
import io


class TestMakeBoss(TestCase):
    @patch('game.choice', return_value='Kalzeruth')
    def test_make_boss_correct_boss(self, mock_choice):
        expected_output = {'name': '\x1b[31mKalzeruth\x1b[0m', 'category': 'boss', 'hp': 60, 'damage': 20,
                           'position': [15, 15],
                           'attack_name': ['Massacre', 'Demolish', 'Torture', 'Execute', 'Harvest']}
        self.assertEqual(expected_output, make_boss())

    @patch('random.choice', return_value='Kalzeruth')
    def test_make_boss_correct_type(self, mock_choice):
        make_boss()
        self.assertEqual(dict, type(make_boss()))
