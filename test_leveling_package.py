from unittest import TestCase
from game import leveling_package


class TestLevelingPackage(TestCase):

    def test_player_experience_goes_up_100(self):
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
        leveling_package(player)
        actual = player
        expected = {'category': 'player',
                    'class': 'Warrior',
                    'class_dictionary': {'accuracy_rate': 50,
                                         'attack_name': 'Threaten',
                                         'base_damage_max': 12,
                                         'base_damage_min': 7,
                                         'experience_needed': 200,
                                         'level': 1,
                                         'level_name': 'Apprentice Warrior',
                                         'max_hp': 20},
                    'experience': 100,
                    'hp': 20,
                    'level': 1,
                    'name': 'Leo',
                    'position': [0, 0]}
        self.assertEqual(actual, expected)

    def test_player_level_change_based_on_experience(self):
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
                  'experience': 400,
                  'hp': 20,
                  'level': 2,
                  'name': 'Leo',
                  'position': [0, 0]}
        leveling_package(player)
        actual = player
        expected = {'category': 'player',
                    'class': 'Warrior',
                    'class_dictionary': {'accuracy_rate': 50,
                                         'attack_name': "Heaven's Hammer",
                                         'base_damage_max': 24,
                                         'base_damage_min': 18,
                                         'level': 3,
                                         'level_name': 'Paladin',
                                         'max_hp': 40},
                    'experience': 500,
                    'hp': 20,
                    'level': 3,
                    'name': 'Leo',
                    'position': [0, 0]}
        self.assertEqual(actual, expected)

    def test_player_class_dictionary_change_based_on_experience(self):
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
                  'experience': 400,
                  'hp': 20,
                  'level': 2,
                  'name': 'Leo',
                  'position': [0, 0]}
        leveling_package(player)
        actual = player
        expected = {'category': 'player',
                    'class': 'Warrior',
                    'class_dictionary': {'accuracy_rate': 50,
                                         'attack_name': "Heaven's Hammer",
                                         'base_damage_max': 24,
                                         'base_damage_min': 18,
                                         'level': 3,
                                         'level_name': 'Paladin',
                                         'max_hp': 40},
                    'experience': 500,
                    'hp': 20,
                    'level': 3,
                    'name': 'Leo',
                    'position': [0, 0]}
        self.assertEqual(actual, expected)
