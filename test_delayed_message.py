from unittest import TestCase
from unittest.mock import patch
from game import delayed_message
import io


class TestDelayedMessage(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delayed_message_shows_correct_message(self, mock_stdout):
        delayed_message("Hello", 1)
        expected = "Hello\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delayed_message_shows_correct_type(self, mock_stdout):
        delayed_message("Hello", 1)
        self.assertEqual(type(mock_stdout.getvalue()), str)
