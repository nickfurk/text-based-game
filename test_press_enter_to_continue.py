from unittest import TestCase
from unittest.mock import patch
from game import press_enter_to_continue
import io

class TestPressEnterToContinue(TestCase):
    @patch('builtins.input', side_effect=[''])
    def test_press_enter_to_continue_output(self, mock_input):
        actual = press_enter_to_continue()
        expected_output = None
        self.assertEqual(expected_output, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_press_enter_to_continue_correct(self, mock_stdout, mock_input):
        expected_output = ''
        press_enter_to_continue()
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['Okay', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_press_enter_to_continue_error(self, mock_stdout, mock_input):
        expected_output = 'Please press enter!\n'
        press_enter_to_continue()
        self.assertEqual(expected_output, mock_stdout.getvalue())
