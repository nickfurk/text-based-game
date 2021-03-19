from unittest import TestCase
from unittest.mock import patch
from game import random_monster
import game
import io

class TestRandomMonster(TestCase):
    @patch('game.LIST_OF_MONSTERS', return_value=['Zelda'])
    @patch('game.LIST_OF_MONSTER_TYPES', return_value=['Cat'])
    @patch('game.MONSTER_HP', return_value={1: {'level': 1, 'hp': 10}, 2: {'level': 2, 'hp': 10 + 5},
                                            3: {'level': 3, 'hp': 10 + 5 * 2}})
    @patch('game.MONSTER_DAMAGE', return_value={1: {'level': 1, 'damage': 10}, 2: {'level': 2, 'damage': 10 + 5},
                                                3: {'level': 3, 'damage': 10 + 5 * 2}})
    def test_random_monster_level_one(self, mock_damage, mock_hp, mock_type, mock_name):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = {'name': 'Zelda', 'type': 'Cat', 'hp': 10, 'category': 'monster', 'damage': 10}
        actual = random_monster(player)
        self.assertEqual(expected_output, actual)

    @patch('game.LIST_OF_MONSTERS', return_value=['NickFurry'])
    @patch('game.LIST_OF_MONSTER_TYPES', return_value=['Tiger'])
    @patch('game.MONSTER_HP', return_value={1: {'level': 1, 'hp': 10}, 2: {'level': 2, 'hp': 10 + 5},
                                            3: {'level': 3, 'hp': 10 + 5 * 2}})
    @patch('game.MONSTER_DAMAGE', return_value={1: {'level': 1, 'damage': 10}, 2: {'level': 2, 'damage': 10 + 5},
                                                3: {'level': 3, 'damage': 10 + 5 * 2}})
    def test_random_monster_level_two(self, mock_damage, mock_hp, mock_type, mock_name):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 300,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = {'name': 'NickFurry', 'type': 'Tiger', 'hp': 15, 'category': 'monster', 'damage': 15}
        actual = random_monster(player)
        self.assertEqual(expected_output, actual)
