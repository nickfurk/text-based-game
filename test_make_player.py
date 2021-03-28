from unittest import TestCase
from unittest.mock import patch
from game import make_player


class TestMakePlayer(TestCase):
    @patch('game.player_name_generator', side_effect=["player"])
    @patch('game.input_checker', side_effect=["Warrior"])
    def test_make_player_return_correct_player_dictionary(self, mock_input, mock_generator):
        expected = {'category': 'player',
                    'class': 'Warrior',
                    'class_dictionary': {'accuracy_rate': 50,
                                         'attack_name': 'Threaten',
                                         'base_damage_max': 10,
                                         'base_damage_min': 5,
                                         'experience_needed': 400,
                                         'level': 1,
                                         'level_name': 'Apprentice Warrior',
                                         'max_hp': 20},
                    'experience': 0,
                    'hp': 20,
                    'level': 1,
                    'name': '\u001b[32;1mplayer\u001b[0m',
                    'position': [0, 0]}
        self.assertEqual(make_player(), expected)

    @patch('game.player_name_generator', side_effect=["player"])
    @patch('game.input_checker', side_effect=["Warrior"])
    def test_make_player_return_type(self, mock_input, mock_generator):
        self.assertEqual(type(make_player()), dict)
