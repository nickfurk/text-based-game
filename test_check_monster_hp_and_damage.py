from unittest import TestCase
from unittest.mock import patch
from game import check_monster_hp_and_damage


class TestCheckMonsterHpAndDamage(TestCase):
    @patch('game.MONSTER_DAMAGE', return_value={1: {'level': 1, 'damage': 10}, 2: {'level': 2, 'damage': 10 + 5},
                                                3: {'level': 3, 'damage': 10 + 5 * 2}})
    @patch('game.MONSTER_HP', return_value={1: {'level': 1, 'hp': 10}, 2: {'level': 2, 'hp': 10 + 5},
                                            3: {'level': 3, 'hp': 10 + 5 * 2}})
    def test_check_monster__hp_and_damage_change_equivalent_to_level_2(self, mock_hp, mock_damage):
        player = {'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 10, 'category': 'monster', 'damage': 10}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster', 'damage': 15}
        actual = monster
        self.assertEqual(expected, actual)

    @patch('game.MONSTER_DAMAGE', return_value={1: {'level': 1, 'damage': 10}, 2: {'level': 2, 'damage': 10 + 5},
                                                3: {'level': 3, 'damage': 10 + (5 * 2)}})
    @patch('game.MONSTER_HP', return_value={1: {'level': 1, 'hp': 10}, 2: {'level': 2, 'hp': 10 + 5},
                                            3: {'level': 3, 'hp': 10 + 5 * 2}})
    def test_check_monster_damage_change_equivalent_to_level_3(self, mock_hp, mock_damage):
        player = {'class': 'Warrior', 'hp': 30, 'position': [0, 0], 'level': 3, 'experience': 1000,
                  'category': 'player', 'class_dictionary': {'level': 3, 'level_name': 'Apprentice Warrior',
                                                             'attack_name': 'Havens Hammer',
                                                             'max_hp': 30, 'base_damage_min': 18, 'base_damage_max': 24,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster', 'damage': 15}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 20, 'category': 'monster', 'damage': 20}
        actual = monster
        self.assertEqual(expected, actual)

    @patch('game.MONSTER_DAMAGE', return_value={1: {'level': 1, 'damage': 10}, 2: {'level': 2, 'damage': 10 + 5},
                                                3: {'level': 3, 'damage': 10 + 5 * 2}})
    @patch('game.MONSTER_HP', return_value={1: {'level': 1, 'hp': 10}, 2: {'level': 2, 'hp': 10 + 5},
                                            3: {'level': 3, 'hp': 10 + 5 * 2}})
    def test_check_monster_damage_no_change(self, mock_hp, mock_damage):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster', 'damage': 15}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster', 'damage': 15}
        actual = monster
        self.assertEqual(expected, actual)
