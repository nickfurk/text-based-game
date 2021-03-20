from unittest import TestCase
from game import return_class_dictionary


class TestReturnClassDictionary(TestCase):

    def test_return_class_mage(self):
        player_info = {"class": "Mage"}
        actual = return_class_dictionary(player_info)
        expected = {1: {'accuracy_rate': 25,
                        'attack_name': 'Fireball',
                        'base_damage_max': 20,
                        'base_damage_min': 15,
                        'experience_needed': 500,
                        'level': 1,
                        'level_name': 'Apprentice Mage',
                        'max_hp': 20},
                    2: {'accuracy_rate': 40,
                        'attack_name': 'Firestorm',
                        'base_damage_max': 25,
                        'base_damage_min': 20,
                        'experience_needed': 1000,
                        'level': 2,
                        'level_name': 'Mage',
                        'max_hp': 30},
                    3: {'accuracy_rate': 50,
                        'attack_name': 'Hellfire',
                        'base_damage_max': 30,
                        'base_damage_min': 25,
                        'level': 3,
                        'level_name': 'Arch Mage',
                        'max_hp': 40}}
        self.assertEqual(expected, actual)

    def test_return_class_thief(self):
        player_info = {"class": "Thief"}
        actual = return_class_dictionary(player_info)
        expected = {1: {'accuracy_rate': 85,
                        'attack_name': 'Pickpocket',
                        'base_damage_max': 5,
                        'base_damage_min': 1,
                        'experience_needed': 100,
                        'level': 1,
                        'level_name': 'Apprentice Thief',
                        'max_hp': 20},
                    2: {'accuracy_rate': 95,
                        'attack_name': 'Boomerang Step',
                        'base_damage_max': 10,
                        'base_damage_min': 5,
                        'experience_needed': 300,
                        'level': 2,
                        'level_name': 'Bandit',
                        'max_hp': 30},
                    3: {'accuracy_rate': 100,
                        'attack_name': 'Assassinate',
                        'base_damage_max': 15,
                        'base_damage_min': 10,
                        'level': 3,
                        'level_name': 'Hermit',
                        'max_hp': 40}}
        self.assertEqual(expected, actual)

    def test_return_class_ranger(self):
        player_info = {"class": "Ranger"}
        actual = return_class_dictionary(player_info)
        expected = {1: {'accuracy_rate': 50,
                        'attack_name': 'Iron Arrow',
                        'base_damage_max': 10,
                        'base_damage_min': 5,
                        'experience_needed': 500,
                        'level': 1,
                        'level_name': 'Apprentice Ranger',
                        'max_hp': 20},
                    2: {'accuracy_rate': 60,
                        'attack_name': 'Mortal Blow',
                        'base_damage_max': 15,
                        'base_damage_min': 10,
                        'experience_needed': 1000,
                        'level': 2,
                        'level_name': 'Sniper',
                        'max_hp': 30},
                    3: {'accuracy_rate': 75,
                        'attack_name': "Dragon's Breath",
                        'base_damage_max': 20,
                        'base_damage_min': 15,
                        'level': 3,
                        'level_name': 'Marksman',
                        'max_hp': 40}}
        self.assertEqual(expected, actual)

    def test_return_class_warrior(self):
        player_info = {"class": "Warrior"}
        actual = return_class_dictionary(player_info)
        expected = {1: {'accuracy_rate': 50,
                        'attack_name': 'Threaten',
                        'base_damage_max': 12,
                        'base_damage_min': 7,
                        'experience_needed': 200,
                        'level': 1,
                        'level_name': 'Apprentice Warrior',
                        'max_hp': 20},
                    2: {'accuracy_rate': 50,
                        'attack_name': 'Power Crash',
                        'base_damage_max': 18,
                        'base_damage_min': 12,
                        'experience_needed': 500,
                        'level': 2,
                        'level_name': 'Knight',
                        'max_hp': 30},
                    3: {'accuracy_rate': 50,
                        'attack_name': "Heaven's Hammer",
                        'base_damage_max': 24,
                        'base_damage_min': 18,
                        'level': 3,
                        'level_name': 'Paladin',
                        'max_hp': 40}}
        self.assertEqual(expected, actual)
