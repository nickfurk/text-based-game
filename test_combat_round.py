from unittest import TestCase
from unittest.mock import patch
from game import combat_round
import game
import io


class TestCombatRound(TestCase):
    @patch('game.roll_die', return_value=1)
    @patch('game.fight_or_run_decision', return_value="Yes")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=1)
    @patch('game.run_away_monster', return_value=False)
    @patch('game.run_or_fight_again', return_value="Yes")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_fight_to_death(self, mock_stdout, mock_continue, mock_fight_again, mock_monster_run, mock_damage,
                                  mock_attack_order, mock_decision, mock_roll_die):
        monster = {"name": "Zelda", "hp": 1}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = "Paul has done 1 damage to Zelda!\n" \
                          "Zelda has 0 hp left!\n\n"
        combat_round(player, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('game.roll_die', return_value=1)
    @patch('game.fight_or_run_decision', return_value="Yes")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=1)
    @patch('game.run_or_fight_again', return_value="Yes")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_monster_runaway(self, mock_stdout, mock_continue, mock_fight_again, mock_damage,
                                          mock_attack_order, mock_decision, mock_roll_die):
        monster = {"name": "Zelda", "hp": 2, "damage": 1}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = "Paul has done 1 damage to Zelda!\n" \
                          "Zelda has 1 hp left!\n\n" \
                          "Zelda has done 1 damage to Paul!\n" \
                          "Paul has 19 hp left!\n\n" \
                          "Zelda ran away!\n"
        combat_round(player, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('game.roll_die', return_value=3)
    @patch('game.fight_or_run_decision', return_value="No")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=1)
    @patch('game.run_away_monster', return_value=False)
    @patch('game.run_or_fight_again', return_value="No")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_player_run_before_combat(self, mock_stdout, mock_continue, mock_fight_again, mock_monster_run,
                                                   mock_damage, mock_attack_order, mock_decision, mock_roll_die):
        monster = {"name": "Zelda", "hp": 2, "damage": 1}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = "You've run away successfully from Zelda!\n" \
                          "You were very lucky this time...\n\n"
        combat_round(player, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('game.roll_die', return_value=3)
    @patch('game.fight_or_run_decision', return_value="Yes")
    @patch('game.battle_attack_order', return_value=True)
    @patch('game.player_damage', return_value=1)
    @patch('game.run_away_monster', return_value=False)
    @patch('game.run_or_fight_again', return_value="No")
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_player_run_after_round(self, mock_stdout, mock_continue, mock_fight_again, mock_monster_run,
                                                 mock_damage, mock_attack_order, mock_decision, mock_roll_die):
        monster = {"name": "Zelda", "hp": 2, "damage": 1}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = "Paul has done 1 damage to Zelda!\n" \
                          "Zelda has 1 hp left!\n\n" \
                          "Zelda has done 3 damage to Paul!\n" \
                          "Paul has 17 hp left!\n\n" \
                          "You've run away successfully from Zelda!\n" \
                          "You were very lucky this time...\n\n"
        combat_round(player, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
