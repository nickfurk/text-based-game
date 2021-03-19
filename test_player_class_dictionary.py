from unittest import TestCase
from game import player_class_dictionary
from game import PLAYER_BASE_HP, MAGE_HP_INCREMENT, player_class_dictionary


class TestPlayerClassDictionary(TestCase):


    def test_player_class_dictionary(self):
        player_dict = {"class": "Mage", "experience": 500, "class_dictionary": ""}
        player_class_dictionary(player_dict)
        actual = player_dict
        expected = {'class': 'Mage',
                    'class_dictionary': {'accuracy_rate': 40,
                      'attack_name': 'Firestorm',
                      'base_damage_max': 25,
                      'base_damage_min': 20,
                      'experience_needed': 1000,
                      'level': 2,
                      'level_name': 'Mage',
                      'max_hp': 30},
                    'experience': 500,
                    'level': 2}
        self.assertEqual(actual, expected)