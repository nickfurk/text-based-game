from unittest import TestCase
from unittest.mock import patch
from game import player_damage


class TestPlayerDamage(TestCase):
    @patch('game.randint', return_value=60)
    def test_player_damage_no_damage_returns(self, random_number_generator):
        player = {'category': 'player',
                  'class': 'Warrior',
                  'class_dictionary': {'accuracy_rate': 50,
                                       'attack_name': 'Threaten',
                                       'base_damage_max': 12,
                                       'base_damage_min': 7,
                                       'experience_needed': 200,
                                       'level': 1,
                                       'level_name': 'Apprentice Warrior',
                                       'max_hp': 20},
                  'experience': 0,
                  'hp': 20,
                  'level': 1,
                  'name': 'Leo',
                  'position': [0, 0]}
        actual = player_damage(player)
        expected = 0
        self.assertEqual(actual, expected)

    @patch('game.randint', side_effect=[30, 12])
    def test_player_damage_damage_returns(self, random_number_generator):
        player = {'category': 'player',
                  'class': 'Warrior',
                  'class_dictionary': {'accuracy_rate': 50,
                                       'attack_name': 'Threaten',
                                       'base_damage_max': 12,
                                       'base_damage_min': 7,
                                       'experience_needed': 200,
                                       'level': 1,
                                       'level_name': 'Apprentice Warrior',
                                       'max_hp': 20},
                  'experience': 0,
                  'hp': 20,
                  'level': 1,
                  'name': 'Leo',
                  'position': [0, 0]}
        actual = player_damage(player)
        expected = 12
        self.assertEqual(actual, expected)

    @patch('game.randint', side_effect=[30, 12])
    def test_player_damage_damage_is_integer(self, random_number_generator):
        player = {'category': 'player',
                  'class': 'Warrior',
                  'class_dictionary': {'accuracy_rate': 50,
                                       'attack_name': 'Threaten',
                                       'base_damage_max': 12,
                                       'base_damage_min': 7,
                                       'experience_needed': 200,
                                       'level': 1,
                                       'level_name': 'Apprentice Warrior',
                                       'max_hp': 20},
                  'experience': 0,
                  'hp': 20,
                  'level': 1,
                  'name': 'Leo',
                  'position': [0, 0]}
        self.assertEqual(type(player_damage(player)), int)
