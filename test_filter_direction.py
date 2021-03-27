from unittest import TestCase
from game import filter_direction


class TestFilterDirection(TestCase):
    def test_filter_direction_west_false(self):
        direction = {"direction": "West", "position": 0}
        expected = False
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_west_true(self):
        direction = {"direction": "West", "position": 24}
        expected = True
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_east_false(self):
        direction = {"direction": "East", "position": 24}
        expected = False
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_east_true(self):
        direction = {"direction": "East", "position": 0}
        expected = True
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_south_false(self):
        direction = {"direction": "South", "position": 24}
        expected = False
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_south_true(self):
        direction = {"direction": "South", "position": 0}
        expected = True
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_north_false(self):
        direction = {"direction": "North", "position": 0}
        expected = False
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_north_true(self):
        direction = {"direction": "North", "position": 24}
        expected = True
        self.assertEqual(filter_direction(direction), expected)

    def test_filter_direction_quit(self):
        direction = {"direction": "Quit"}
        expected = True
        self.assertEqual(filter_direction(direction), expected)
