from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_bool(self):
        self.assertEqual(type(validate_move([1, 2], "N")), bool)

    def test_validate_move_valid_north(self):
        expected_output = validate_move([24, 21], "N")
        self.assertEqual(expected_output, False)

    def test_validate_move_invalid_north(self):
        expected_output = validate_move([0, 2], "N")
        self.assertEqual(expected_output, True)

    def test_validate_move_valid_south(self):
        expected_output = validate_move([0, 2], "S")
        self.assertEqual(expected_output, False)

    def test_validate_move_invalid_south(self):
        expected_output = validate_move([24, 21], "S")
        self.assertEqual(expected_output, True)

    def test_validate_move_valid_west(self):
        expected_output = validate_move([3, 24], "W")
        self.assertEqual(expected_output, False)

    def test_validate_move_invalid_west(self):
        expected_output = validate_move([15, 0], "W")
        self.assertEqual(expected_output, True)

    def test_validate_move_valid_east(self):
        expected_output = validate_move([15, 0], "E")
        self.assertEqual(expected_output, False)

    def test_validate_move_invalid_east(self):
        expected_output = validate_move([3, 24], "E")
        self.assertEqual(expected_output, True)

    def test_validate_move_quit(self):
        expected_output = validate_move([0, 0], "quit")
        self.assertEqual(expected_output, False)
