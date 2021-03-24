from unittest import TestCase
from unittest.mock import patch
from game import display_info
import game
import io


class TestDisplayInfo(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_info_correct_print(self, mock_stdout):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        board = {(0, 0): {"location_description": "The room is lit by the light seeping through from the previous "
                                                  "location, but you instantly feel the difference in the atmosphere "
                                                  "already. For some reason, you are just a bit more cold."}}
        expected = "Location: [0, 0]\n" \
                   "Description: The room is lit by the light seeping through from the previous location, " \
                   "but you instantly feel the difference in the atmosphere already. For some reason, you are just a " \
                   "bit more cold.\n" \
                   "Health point: 20/20\n" \
                   "Level: 1, Apprentice Warrior\n" \
                   "Experience: 0/200\n"
        display_info(player, board)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_info_type(self, mock_stdout):
        player = {'name': 'Paul', 'class': 'Warrior', 'hp': 20, 'position': [0, 0], 'level': 1, 'experience': 0,
                  'category': 'player', 'class_dictionary': {'level': 1, 'level_name': 'Apprentice Warrior',
                                                             'experience_needed': 200, 'attack_name': 'Threaten',
                                                             'max_hp': 20, 'base_damage_min': 7, 'base_damage_max': 12,
                                                             'accuracy_rate': 50}}
        board = {(0, 0): {"location_description": "The room is lit by the light seeping through from the previous "
                                                  "location, but you instantly feel the difference in the atmosphere "
                                                  "already. For some reason, you are just a bit more cold."}}
        display_info(player, board)
        self.assertEqual(type(mock_stdout.getvalue()), str)
