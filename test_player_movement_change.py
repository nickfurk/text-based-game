from unittest import TestCase
from game import player_movement_change

class TestPlayerMovementChange(TestCase):
    def test_player_movement_change_list(self):
        expected_output = player_movement_change([1, 2], "N")
        self.assertEqual(type(expected_output), list)

    def test_player_movement_change_north(self):
        expected_output = player_movement_change([1, 2], "N")
        self.assertEqual(expected_output, [0, 2])

    def test_player_movement_change_south(self):
        expected_output = player_movement_change([1, 2], "S")
        self.assertEqual(expected_output, [2, 2])

    def test_player_movement_change_west(self):
        expected_output = player_movement_change([1, 2], "W")
        self.assertEqual(expected_output, [1, 1])

    def test_player_movement_change_east(self):
        expected_output = player_movement_change([1, 2], "E")
        self.assertEqual(expected_output, [1, 3])
