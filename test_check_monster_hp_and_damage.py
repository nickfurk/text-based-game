from unittest import TestCase
from unittest.mock import patch
from game import check_monster_hp_and_damage


class TestCheckMonsterHpAndDamage(TestCase):

    @patch('game.randint', return_value=12)
    def test_check_monster_hp_and_damage_change_equivalent_to_level_2(self, mock_random_number):
        player = {'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 10, 'category': 'monster', 'damage': 10}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 17, 'category': 'monster', 'damage': 12}
        actual = monster
        self.assertEqual(expected, actual)

    @patch('game.randint', return_value=17)
    def test_check_monster_hp_and_damage_change_equivalent_to_level_3(self, mock_random_number):
        player = {'class': 'Warrior', 'hp': 30, 'position': [0, 0], 'level': 3, 'experience': 1000,
                  'category': 'player', 'class_dictionary': {'level': 3, 'level_name': 'Apprentice Warrior',
                                                             'attack_name': 'Havens Hammer',
                                                             'max_hp': 30, 'base_damage_min': 18, 'base_damage_max': 24,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 15, 'category': 'monster', 'damage': 15}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 24, 'category': 'monster', 'damage': 17}
        actual = monster
        self.assertEqual(expected, actual)

    @patch('game.randint', return_value=17)
    def test_check_monster_hp_no_change(self, mock_random_number):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 2, 'experience': 400,
                  'category': 'player', 'class_dictionary': {'level': 2, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 500, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        monster = {'name': 'Zelda', 'type': 'Cat', 'hp': 17, 'category': 'monster', 'damage': 17}
        check_monster_hp_and_damage(player, monster)
        expected = {'name': 'Zelda', 'type': 'Cat', 'hp': 17, 'category': 'monster', 'damage': 17}
        actual = monster
        self.assertEqual(expected, actual)
