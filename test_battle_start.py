from unittest import TestCase
from unittest.mock import patch
from game import battle_start


class TestBattleStart(TestCase):

    @patch('game.player_damage', return_value=5)
    def test_player_attacks_first_both_sides_lose_hp(self, mock_player_damage):
        monster = {"name": "Zelda", "hp": 10, "damage": 5}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        battle_start(player, monster, True)
        self.assertTrue(monster["hp"] != 10, player["hp"] != 20)

    @patch('game.player_damage', return_value=5)
    def test_monster_attacks_first_both_sides_lose_hp(self, mock_player_damage):
        monster = {"name": "Zelda", "hp": 10, "damage": 5}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        battle_start(player, monster, False)
        self.assertTrue(monster["hp"] != 10, player["hp"] != 20)

    @patch('game.player_damage', return_value=10)
    def test_player_attacks_first_monster_dies(self, mock_player_damage):
        monster = {"name": "Zelda", "hp": 10, "damage": 5}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        battle_start(player, monster, True)
        self.assertTrue(monster["hp"] == 0, player["hp"] == 20)

    @patch('game.player_damage', return_value=10)
    def test_player_attacks_first_monster_dies_player_experience_increase_100(self, mock_player_damage):
        monster = {"name": "Zelda", "hp": 10, "damage": 5}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        battle_start(player, monster, True)
        self.assertTrue(monster["hp"] == 0, player["experience"] == 100)

    def test_monster_attacks_player_dies_no_hp(self):
        monster = {"name": "Zelda", "hp": 10, "damage": 5}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 1, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        battle_start(player, monster, False)
        self.assertTrue(monster["hp"] == 10, player["hp"] == 0)
