from unittest import TestCase
from game import change_dict_to_list


class TestChangeDictToList(TestCase):
    def test_change_dict_to_list_type(self):
        test_dict = [{'direction': 'West'}, {'direction': 'East'}, {'direction': 'South'}, {'direction': 'North'},
                     {'direction': 'Quit'}]
        self.assertEqual(type(change_dict_to_list(test_dict)), list)

    def test_change_dict_to_list_return_correct_list(self):
        test_dict = [{'direction': 'West'}, {'direction': 'East'}, {'direction': 'South'}, {'direction': 'North'},
                     {'direction': 'Quit'}]
        expected = ['West', 'East', 'South', 'North', 'Quit']
        self.assertEqual(change_dict_to_list(test_dict), expected)

    def test_change_dict_to_list_return_correct_length(self):
        test_dict = [{'direction': 'East'}, {'direction': 'South'}, {'direction': 'Quit'}]
        expected = ['East', 'South', 'Quit']
        self.assertEqual(len(change_dict_to_list(test_dict)), len(expected))
