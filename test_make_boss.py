from unittest import TestCase
from unittest.mock import patch
from game import make_boss
import game
import io


class TestMakeBoss(TestCase):
    @patch('game.PICK_RANDOM_BOSS_NAME', return_value='Lord Zelda')
    @patch('game.BOSS_MAX_HP', return_value=30)
    @patch('game.BOSS_MAX_DAMAGE', return_value=15)
    @patch('game.BOSS_POSITION', return_value=[2, 3])
    @patch('game.RANDOM_BOSS_ATTACK', return_value='Meow')
    def test_make_boss_correct_boss(self, mock_attack, mock_position, mock_damage, mock_hp, mock_name):
        expected_output = {'name': '\x1b[31mLord Zelda\x1b[0m', 'category': 'boss', 'hp': 30, 'damage': 15,
                           'position': [2, 3], 'attack_name': 'Meow'}
        self.assertEqual(expected_output, make_boss())

    @patch('game.PICK_RANDOM_BOSS_NAME', return_value='Lord Zelda')
    @patch('game.BOSS_MAX_HP', return_value=30)
    @patch('game.BOSS_MAX_DAMAGE', return_value=15)
    @patch('game.BOSS_POSITION', return_value=[2, 3])
    @patch('game.RANDOM_BOSS_ATTACK', return_value='Meow')
    def test_make_boss_correct_type(self, mock_attack, mock_position, mock_damage, mock_hp, mock_name):
        make_boss()
        self.assertEqual(dict, type(make_boss()))
