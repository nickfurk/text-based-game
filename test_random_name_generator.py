from unittest import TestCase
from unittest.mock import patch
from game import random_name_generator
import io
from coolname import generate


class TestRandomNameGenerator(TestCase):
    @patch('builtins.input', side_effect=["1"])
    @patch('game.generate', side_effect=[['Stirring', 'Lyrebird']])
    def test_random_name_generator_select_generated_name(self, mock_generate, mock_input):
        actual = random_name_generator()
        expected = "Stirring Lyrebird"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["2"])
    def test_random_name_generator_select_choose_another_random_name(self, mock_input):
        actual = random_name_generator()
        expected = "I would like to choose another one at random"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["3"])
    def test_random_name_generator_select_choose_own_name(self, mock_input):
        actual = random_name_generator()
        expected = "I would like to choose my own name!"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1"])
    @patch('game.generate', side_effect=[['Stirring', 'Lyrebird']])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_name_generator_correct_print(self, mock_stdout, mock_generate, mock_input):
        expected = "\n\u001b[32;1mStirring Lyrebird\u001b[0m was created randomly! Would you like to choose your " \
                   "own name or create another at random?\n\n" \
                   "{1: 'I would like to choose this name!'\n" \
                   " 2: 'I would like to choose another one at random'\n" \
                   " 3: 'I would like to choose my own name!'}\n"
        random_name_generator()
        self.assertEqual(expected, mock_stdout.getvalue())
