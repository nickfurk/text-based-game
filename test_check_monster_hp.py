from unittest import TestCase
from unittest.mock import patch
from game import check_monster_hp

class TestCheckMonsterHp(TestCase):
    @patch('game.MONSTER_HP', return_value={1: {'level': 1, 'hp': 10}, 2: {'level': 2, 'hp': 10 + 5},
                                            3: {'level': 3, 'hp': 10 + 5 * 2}})
    def test_check_monster_hp_change(self, mock_hp):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 200,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 10, 'category': 'monster'}
        check_monster_hp(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster'}
        actual = monster
        self.assertEqual(expected, actual)

    @patch('game.MONSTER_HP', return_value={1: {'level': 1, 'hp': 10}, 2: {'level': 2, 'hp': 10 + 5},
                                            3: {'level': 3, 'hp': 10 + 5 * 2}})
    def test_check_monster_hp_no_change(self, mock_hp):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 200,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster'}
        check_monster_hp(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster'}
        actual = monster
        self.assertEqual(expected, actual)