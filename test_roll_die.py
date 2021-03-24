from unittest import TestCase
from game import roll_die


class TestRollDie(TestCase):
    def test_roll_die_six_sided_once(self):
        actual = roll_die(1, 6)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 6)

    def test_roll_die_hundred_sided_once(self):
        actual = roll_die(1, 100)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 100)

    def test_roll_die_ten_sided_twice(self):
        actual = roll_die(2, 10)
        self.assertGreaterEqual(actual, 2)
        self.assertLessEqual(actual, 20)

    def test_roll_die_two_sided_hundred_times(self):
        actual = roll_die(100, 2)
        self.assertGreaterEqual(actual, 100)
        self.assertLessEqual(actual, 200)
