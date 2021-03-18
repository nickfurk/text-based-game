from unittest import TestCase
from unittest.mock import patch
from game import input_checker


class TestInputChecker(TestCase):

    @patch('builtins.input', side_effect=['3'])
    def test_correct_option_string_is_return(self, mock_input):
        options = {'1': 'Mage', '2': 'Thief', '3': 'Ranger', '4': 'Warrior'}
        print_this = input_checker(options)
        expected_output = 'Ranger'
        self.assertEqual(expected_output, print_this)