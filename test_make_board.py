from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):
    @patch('game.BOARD_SIZE', return_value=2)
    def test_make_board(self, mock_board):
        actual = make_board()
        expected = {(0, 0): {'location_description': 'The room is lit by the light seeping '
                                                     'through from the previous location, but you '
                                                     'instantly feel the\n'
                                                     '             difference in the atmosphere '
                                                     'already. For some reason, you are just a '
                                                     'bit more cold.'},
                    (0, 1): {'location_description': 'You start to move on an instinct as the '
                                                     'seeping light no longer covers the entirety '
                                                     'of the room\n'
                                                     '             anymore. You start to feel a '
                                                     'shiver up your spine every step you take.'},
                    (1, 0): {'location_description': 'This room is surprisingly warm... You '
                                                     'wonder why...'},
                    (1, 1): {'location_description': 'You start to feel more paranoid as time '
                                                     'passes, and keep thinking back on your life '
                                                     'and whether\n'
                                                     "             or not you'll be able to get "
                                                     'out of here alive'}}
        self.assertEqual(actual, expected)
