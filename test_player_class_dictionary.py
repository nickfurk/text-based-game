from unittest import TestCase
from game import player_class_dictionary


class TestPlayerClassDictionary(TestCase):
    def test_player_class_dictionary_updates(self):
        player_dict = {"class": "Mage", "experience": 500, "class_dictionary": ""}
        player_class_dictionary(player_dict)
        actual = player_dict
        expected = {'class': 'Mage',
                    'class_dictionary': {'accuracy_rate': 55,
                                         'attack_name': 'Firestorm',
                                         'base_damage_max': 25,
                                         'base_damage_min': 20,
                                         'experience_needed': 600,
                                         'level': 2,
                                         'level_name': 'Mage',
                                         'max_hp': 25},
                    'experience': 500,
                    'level': 2}
        self.assertEqual(actual, expected)

    def test_player_class_dictionary_level_updates(self):
        player_dict = {"class": "Mage", "experience": 500, "class_dictionary": "", "level": 1}
        player_class_dictionary(player_dict)
        actual = player_dict
        expected = {'class': 'Mage',
                    'class_dictionary': {'accuracy_rate': 55,
                                         'attack_name': 'Firestorm',
                                         'base_damage_max': 25,
                                         'base_damage_min': 20,
                                         'experience_needed': 600,
                                         'level': 2,
                                         'level_name': 'Mage',
                                         'max_hp': 25},
                    'experience': 500,
                    'level': 2}
        self.assertEqual(actual, expected)

