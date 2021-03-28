from unittest import TestCase
from game import leveling_package


class TestLevelingPackage(TestCase):
    def test_leveling_package_player_level_and_dictionary_change_based_on_experience(self):
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
                                         'attack_name': 'Power Crash',
                                         'base_damage_max': 15,
                                         'base_damage_min': 10,
                                         'experience_needed': 700,
                                         'level': 2,
                                         'level_name': 'Knight',
                                         'max_hp': 50},
                    'experience': 400,
                    'hp': 20,
                    'level': 2,
                    'name': 'Leo',
                    'position': [0, 0]}
        self.assertEqual(actual, expected)
