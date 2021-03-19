from unittest import TestCase
from unittest.mock import patch
from game import check_monster_damage


class TestCheckMonsterDamage(TestCase):
    @patch('game.MONSTER_DAMAGE', return_value={1: {'level': 1, 'damage': 10}, 2: {'level': 2, 'damage': 10 + 5},
                                                3: {'level': 3, 'damage': 10 + 5 * 2}})
    def test_check_monster_damage_change(self, mock_damage):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'category': 'monster', 'damage': 10}
        check_monster_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'category': 'monster', 'damage': 15}
        actual = monster
        self.assertEqual(expected, actual)

    @patch('game.MONSTER_DAMAGE', return_value={1: {'level': 1, 'damage': 10}, 2: {'level': 2, 'damage': 10 + 5},
                                                3: {'level': 3, 'damage': 10 + 5 * 2}})
    def test_check_monster_damage_no_change(self, mock_damage):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'category': 'monster', 'damage': 15}
        check_monster_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'category': 'monster', 'damage': 15}
        actual = monster
        self.assertEqual(expected, actual)
