from unittest import TestCase
from unittest.mock import patch
from game import player_game_descriptions
from colorama import Fore, Style
import game
import io


class TestPlayerGameDescriptions(TestCase):
    @patch('game.BOARD_SIZE', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_game_descriptions_print(self, mock_stdout, mock_size):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {"position": [2, 2]}
        board = {(0, 0): {'location_description': 'The room is lit by the light seeping through from the previous '
                                                  'location, but you instantly feel the difference in the atmosphere '
                                                  'already. For some reason, you are just a bit more cold.'}}
        expected_output = Fore.GREEN + '[X]' + Style.RESET_ALL + '[ ][ ][ ]\n[ ][ ][ ][ ]\n[ ][ ]' + Fore.RED + '[#]' \
                          + Style.RESET_ALL + '[ ]\n[ ][ ][ ][ ]\n' \
                                              'Location: [0, 0]\n' \
                                              'Description: The room is lit by the light seeping through from the ' \
                                              'previous location, but you instantly feel the difference in the ' \
                                              'atmosphere already. For some reason, you are just a bit more cold.\n' \
                                              'Health point: 20/20\n' \
                                              'Level: 1, Apprentice Warrior\n' \
                                              'Experience: 0\n'
        player_game_descriptions(player, board, boss)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_game_descriptions_type(self, mock_stdout):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {"position": [2, 2]}
        board = {(0, 0): {'location_description': 'The room is lit by the light seeping through from the previous '
                                                  'location, but you instantly feel the difference in the atmosphere '
                                                  'already. For some reason, you are just a bit more cold.'}}
        player_game_descriptions(player, board, boss)
        self.assertEqual(type(mock_stdout.getvalue()), str)
