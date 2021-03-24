from unittest import TestCase
from unittest.mock import patch
from game import random_monster
import game
import io


class TestRandomMonster(TestCase):
    @patch('game.LIST_OF_MONSTERS', return_value=['Zelda'])
    @patch('game.LIST_OF_MONSTER_TYPES', return_value=['Cat'])
    @patch('game.RANDOM_MONSTER_ATTACK', return_value='Rawr')
    def test_random_monster_level_one(self, mock_attack, mock_type, mock_name):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = {'name': '\x1b[33;1mZelda\x1b[0m', 'type': 'Cat', 'hp': 10, 'category': 'monster',
                           'damage': 10, 'attack_name': 'Rawr'}
        actual = random_monster(player)
        self.assertEqual(expected_output, actual)

    @patch('game.LIST_OF_MONSTERS', return_value=['NickFurry'])
    @patch('game.LIST_OF_MONSTER_TYPES', return_value=['Tiger'])
    @patch('game.RANDOM_MONSTER_ATTACK', return_value='Rawr')
    def test_random_monster_level_two(self, mock_attack, mock_type, mock_name):
        player = {'category': 'player',
                  'class': 'Warrior',
                  'class_dictionary': {'accuracy_rate': 50, 'attack_name': 'Power Crash', 'base_damage_max': 15,
                                       'base_damage_min': 10, 'experience_needed': 700, 'level': 2,
                                       'level_name': 'Knight', 'max_hp': 20},
                  'experience': 500,
                  'hp': 20,
                  'level': 2,
                  'name': '\u001b[32;1mplayer\u001b[0m',
                  'position': [0, 0]}
        expected_output = {'name': '\x1b[33;1mNickFurry\x1b[0m', 'type': 'Tiger', 'hp': 15, 'category': 'monster',
                           'damage': 15, 'attack_name': 'Rawr'}
        actual = random_monster(player)
        self.assertEqual(expected_output, actual)
