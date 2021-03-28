from unittest import TestCase
from unittest.mock import patch
from game import run_away_player
import io


class TestRunAwayPlayer(TestCase):
    @patch('game.roll_die', return_value=1)
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_player_damaged(self, mock_stdout, mock_continue, mock_die):
        monster = {"name": "Zelda", "hp": 2, "damage": 1}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = "You've been damaged \033[4m1\u001b[0m hp by Zelda while running away!" \
                          "\nYou only have 19 hp left! Be careful Paul!\n"
        run_away_player(player, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('game.roll_die', return_value=2)
    @patch('game.press_enter_to_continue', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_player_not_damaged(self, mock_stdout, mock_continue, mock_die):
        monster = {"name": "Zelda", "hp": 2, "damage": 1}
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        expected_output = "You've run away successfully from Zelda!\n" \
                          "You were very lucky this time...\n\n"
        run_away_player(player, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
