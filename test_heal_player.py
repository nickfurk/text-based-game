from unittest import TestCase
from unittest.mock import patch
from game import heal_player
import io


class TestHealPlayer(TestCase):
    def test_heal_player_low_hp(self):
        player = {'hp': 6, 'class_dictionary': {'max_hp': 20}}
        expected_output = 10
        heal_player(player)
        self.assertEqual(expected_output, player['hp'])

    def test_heal_player_high_hp(self):
        player = {'hp': 18, 'class_dictionary': {'max_hp': 20}}
        expected_output = 20
        heal_player(player)
        self.assertEqual(expected_output, player['hp'])

    def test_heal_player_different_max_hp(self):
        player = {'hp': 18, 'class_dictionary': {'max_hp': 25}}
        expected_output = 22
        heal_player(player)
        self.assertEqual(expected_output, player['hp'])

    def test_heal_player_hp_type(self):
        player = {'hp': 18, 'class_dictionary': {'max_hp': 25}}
        heal_player(player)
        self.assertEqual(int, type(player['hp']))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_player_prompt(self, mock_stdout):
        player = {'hp': 18, 'class_dictionary': {'max_hp': 25}}
        expected_output = "It seems like there's no one in the room. You are healed by 4 hp!\n\n"
        heal_player(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
