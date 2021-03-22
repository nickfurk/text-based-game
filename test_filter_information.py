from unittest import TestCase
from unittest.mock import patch
from game import filter_information
import game
import io


class TestFilterInformation(TestCase):
    def test_filter_information_hp(self):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        item = 'hp'
        expected_output = 20
        self.assertEqual(filter_information(player, item), expected_output)

    def test_filter_information_level_name(self):
        player = {'level': 1, 'level_name': 'Apprentice Warrior', 'experience_needed': 200, 'attack_name': 'Threaten',
                  'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12, 'accuracy_rate': 50}
        item = 'level_name'
        expected_output = 'Apprentice Warrior'
        self.assertEqual(filter_information(player, item), expected_output)
