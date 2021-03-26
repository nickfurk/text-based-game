from unittest import TestCase
from unittest.mock import patch
from game import check_monster_hp_and_damage


class TestCheckMonsterHpAndDamage(TestCase):
    def test_check_monster_hp_and_damage_change_equivalent_to_level_2(self):
        player = {'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 10, 'category': 'monster', 'damage': 10}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 17, 'category': 'monster', 'damage': 15}
        actual = monster
        self.assertEqual(expected, actual)

    def test_check_monster_hp_and_damage_change_equivalent_to_level_3(self):
        player = {'class': 'Warrior', 'hp': 30, 'position': [0, 0], 'level': 3, 'experience': 1000,
                  'category': 'player', 'class_dictionary': {'level': 3, 'level_name': 'Apprentice Warrior',
                                                             'attack_name': 'Havens Hammer',
                                                             'max_hp': 30, 'base_damage_min': 18, 'base_damage_max': 24,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster', 'damage': 15}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 24, 'category': 'monster', 'damage': 20}
        actual = monster
        self.assertEqual(expected, actual)

    def test_check_monster_hp_and_damage_no_change(self):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 17, 'category': 'monster', 'damage': 15}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 17, 'category': 'monster', 'damage': 15}
        actual = monster
        self.assertEqual(expected, actual)
