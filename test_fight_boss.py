from unittest import TestCase
from unittest.mock import patch
from game import fight_boss
import game
import io


class TestFightBoss(TestCase):
    @patch('game.roll_die', return_value=1)
    @patch('game.fight_or_run_decision_boss_round', return_value="Yes")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=2)
    @patch('game.run_or_fight_again', return_value="Yes")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_boss_fight_to_death(self, mock_stdout, mock_continue, mock_fight_again, mock_damage,
                                       mock_attack_order, mock_decision, mock_roll_die):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [2, 3], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Lord Zelda', 'hp': 4, 'damage': 15, 'position': [2, 3], "category": "boss",
                "attack_name": ["Scratch"]}
        expected_output = "Paul has used Threaten and has done 2 damage to Lord Zelda!\n" \
                          "Lord Zelda has 2 hp left!\n\n" \
                          "Lord Zelda has used Scratch and has done 1 damage to Paul!\n" \
                          "Paul has 19 hp left!\n\n" \
                          "Paul has used Threaten and has done 2 damage to Lord Zelda!\n" \
                          "Lord Zelda has 0 hp left!\n\n"
        fight_boss(player, boss)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.roll_die', return_value=1)
    @patch('game.fight_or_run_decision_boss_round', return_value="Yes")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=2)
    @patch('game.run_or_fight_again', return_value="Yes")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_boss_player_dead(self, mock_stdout, mock_continue, mock_fight_again, mock_damage,
                                    mock_attack_order, mock_decision, mock_roll_die):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 1, 'position': [2, 3], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Lord Zelda', 'hp': 4, 'damage': 15, 'position': [2, 3], "category": "boss",
                "attack_name": ["Scratch"]}
        expected_output = "Paul has used Threaten and has done 2 damage to Lord Zelda!\n" \
                          "Lord Zelda has 2 hp left!\n\n" \
                          "Lord Zelda has used Scratch and has done 1 damage to Paul!\n" \
                          "Paul has 0 hp left!\n\n"
        fight_boss(player, boss)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.roll_die', return_value=5)
    @patch('game.fight_or_run_decision_boss_round', return_value="Yes")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=2)
    @patch('game.run_or_fight_again', return_value="No")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_boss_run_before_combat(self, mock_stdout, mock_continue, mock_fight_again, mock_damage,
                                          mock_attack_order, mock_decision, mock_roll_die):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [2, 3], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Lord Zelda', 'hp': 4, 'damage': 15, 'position': [2, 3], "category": "boss",
                "attack_name": ["Scratch"]}
        expected_output = "Paul has used Threaten and has done 2 damage to Lord Zelda!\n" \
                          "Lord Zelda has 2 hp left!\n\n" \
                          "Lord Zelda has used Scratch and has done 5 damage to Paul!\n" \
                          "Paul has 15 hp left!\n\n" \
                          "You've run away successfully from Lord Zelda!\n" \
                          "You were very lucky this time...\n\n"
        fight_boss(player, boss)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('game.roll_die', return_value=1)
    @patch('game.fight_or_run_decision_boss_round', return_value="Yes")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=2)
    @patch('game.run_or_fight_again', return_value="No")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_boss_run_after_round(self, mock_stdout, mock_continue, mock_fight_again, mock_damage,
                                        mock_attack_order, mock_decision, mock_roll_die):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [2, 3], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        boss = {'name': 'Lord Zelda', 'hp': 4, 'damage': 15, 'position': [2, 3], "category": "boss",
                "attack_name": ["Scratch"]}
        expected_output = "Paul has used Threaten and has done 2 damage to Lord Zelda!\n" \
                          "Lord Zelda has 2 hp left!\n\n" \
                          "Lord Zelda has used Scratch and has done 1 damage to Paul!\n" \
                          "Paul has 19 hp left!\n\n" \
                          "You've been damaged 1 hp by Lord Zelda while running away!\n" \
                          "You only have 18 hp left! Be careful Paul!\n"
        fight_boss(player, boss)
        self.assertEqual(expected_output, mock_stdout.getvalue())