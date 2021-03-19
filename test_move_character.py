from unittest import TestCase
from unittest.mock import patch
from game import move_character
import game
import io


class TestMoveCharacter(TestCase):
    @patch('game.input_checker', return_value='E')
    @patch('game.player_game_descriptions', return_value='')
    def test_move_character_east(self, mock_description, mock_checker):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Boss Zelda', 'hp': 30, 'damage': 10, 'position': [15, 15]}
        board = {}
        expected_output = [0, 1]
        move_character(player, board, boss)
        self.assertEqual(expected_output, player["position"])

    @patch('game.input_checker', return_value='W')
    @patch('game.player_game_descriptions', return_value='')
    def test_move_character_west(self, mock_description, mock_checker):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 1], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Boss Zelda', 'hp': 30, 'damage': 10, 'position': [15, 15]}
        board = {}
        expected_output = [0, 0]
        move_character(player, board, boss)
        self.assertEqual(expected_output, player["position"])

    @patch('game.input_checker', return_value='N')
    @patch('game.player_game_descriptions', return_value='')
    def test_move_character_north(self, mock_description, mock_checker):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [1, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Boss Zelda', 'hp': 30, 'damage': 10, 'position': [15, 15]}
        board = {}
        expected_output = [0, 0]
        move_character(player, board, boss)
        self.assertEqual(expected_output, player["position"])

    @patch('game.input_checker', return_value='S')
    @patch('game.player_game_descriptions', return_value='')
    def test_move_character_south(self, mock_description, mock_checker):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Boss Zelda', 'hp': 30, 'damage': 10, 'position': [15, 15]}
        board = {}
        expected_output = [1, 0]
        move_character(player, board, boss)
        self.assertEqual(expected_output, player["position"])

    @patch('game.input_checker', return_value='S')
    @patch('game.player_game_descriptions', return_value='')
    def test_move_character_type(self, mock_description, mock_checker):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Boss Zelda', 'hp': 30, 'damage': 10, 'position': [15, 15]}
        board = {}
        move_character(player, board, boss)
        self.assertEqual(list, type(player["position"]))
