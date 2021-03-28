from unittest import TestCase
from unittest.mock import patch
from game import random_monster


class TestRandomMonster(TestCase):
    @patch('game.randint', return_value=8)
    @patch('game.choice', side_effect=['Amputator', 'Ureh Caverns'])
    def test_random_monster_level_one(self, mock_choice, mock_random):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = {'name': '\x1b[33;1mAmputator\x1b[0m', 'type': 'Ureh Caverns', 'hp': 10,
                           'category': 'monster', 'damage': 8, 'attack_name': ['Bite', 'Slash', 'Poisonous Trap']}
        actual = random_monster(player)
        self.assertEqual(expected_output, actual)

    @patch('game.randint', return_value=12)
    @patch('game.choice', side_effect=['Amputator', 'Ureh Caverns'])
    def test_random_monster_level_two(self, mock_choice, mock_random):
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
        expected_output = {'name': '\x1b[33;1mAmputator\x1b[0m', 'type': 'Ureh Caverns', 'hp': 17,
                           'category': 'monster', 'damage': 12, 'attack_name': ['Bite', 'Slash', 'Poisonous Trap']}
        actual = random_monster(player)
        self.assertEqual(expected_output, actual)
