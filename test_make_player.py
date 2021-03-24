from unittest import TestCase
from unittest.mock import patch
from game import make_player


class TestMakePlayer(TestCase):
    @patch('game.player_name_generator', side_effect=["player"])
    @patch('game.player_class_generator', side_effect=['Warrior'])
    @patch('game.player_class_dictionary', side_effect=[{'accuracy_rate': 50, 'attack_name': 'Threaten',
                                                         'base_damage_max': 12, 'base_damage_min': 7,
                                                         'experience_needed': 200, 'level': 1,
                                                         'level_name': 'Apprentice Warrior', 'max_hp': 20}])
    @patch('game.PLAYER_BASE_HP', return_value=20)
    @patch('game.PLAYER_STARTING_POSITION', side_effect=[[0, 0]])
    def test_make_player_return_correct_player_dictionary(self, mock_position, mock_hp, mock_dict, mock_generator, mock_name):
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
                    'name': '\u001b[32;1mplayer\u001b[0m',
                    'position': [0, 0]}
        self.assertEqual(actual, expected)
