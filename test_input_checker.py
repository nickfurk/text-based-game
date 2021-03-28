from unittest import TestCase
from unittest.mock import patch
from game import input_checker
import io


class TestInputChecker(TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_input_checker_correct_option_string_is_return(self, mock_input):
        options = {1: 'Mage', 2: 'Thief', 3: 'Ranger', 4: 'Warrior'}
        print_this = input_checker(options)
        expected_output = 'Ranger'
        self.assertEqual(expected_output, print_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_input_checker_correct_print(self, mock_input, mock_stdout):
        options = {1: 'Mage', 2: 'Thief', 3: 'Ranger', 4: 'Warrior'}
        expected_output = "{1: 'Mage'\n" \
                          " 2: 'Thief'\n" \
                          " 3: 'Ranger'\n" \
                          " 4: 'Warrior'}\n"
        input_checker(options)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
