from unittest import TestCase
from unittest.mock import patch
from game import make_player


class TestMakePlayer(TestCase):

    @patch('builtins.input', side_effect=["leo", "4"])
    def test_return_correct_player_dictionary(self, mock_input):
        actual = make_player()
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
                    'experience': 0,
                    'hp': 20,
                    'level': 1,
                    'name': 'Leo',
                    'position': [0, 0]}
        self.assertEqual(actual, expected)
