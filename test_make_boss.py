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
    def test_make_boss_correct_boss(self, mock_position, mock_damage, mock_hp, mock_name):
        expected_output = {'name': 'Lord Zelda', 'hp': 30, 'damage': 15, 'position': [2, 3]}
        self.assertEqual(expected_output, make_boss())
