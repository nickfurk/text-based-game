from unittest import TestCase
from game import check_level


class TestCheckLevel(TestCase):
    def test_check_level_return_1(self):
        player_info = {"class": "Mage", "experience": 0}
        actual = check_level(player_info)
        expected = 1
        self.assertEqual(actual, expected)

    def test_check_level_return_2(self):
        player_info = {"class": "Mage", "experience": 500}
        actual = check_level(player_info)
        expected = 2
        self.assertEqual(actual, expected)

    def test_check_level_return_3(self):
        player_info = {"class": "Mage", "experience": 1000}
        actual = check_level(player_info)
        expected = 3
        self.assertEqual(actual, expected)

    def test_check_leve_return_integer(self):
        player_info = {"class": "Mage", "experience": 1000}
        actual = check_level(player_info)
        expected = 3
        self.assertEqual(type(actual), type(expected))
