from unittest import TestCase
from game import player_movement_change


class TestPlayerMovementChange(TestCase):
    def test_player_movement_change_list(self):
        current_position = [1, 2]
        player_movement_change(current_position, "N")
        self.assertEqual(type(current_position), list)

    def test_player_movement_change_north(self):
        current_position = [1, 2]
        player_movement_change(current_position, "N")
        self.assertEqual(current_position, [0, 2])

    def test_player_movement_change_south(self):
        current_position = [1, 2]
        player_movement_change(current_position, "S")
        self.assertEqual(current_position, [2, 2])

    def test_player_movement_change_west(self):
        current_position = [1, 2]
        player_movement_change(current_position, "W")
        self.assertEqual(current_position, [1, 1])

    def test_player_movement_change_east(self):
        current_position = [1, 2]
        player_movement_change(current_position, "E")
        self.assertEqual(current_position, [1, 3])
