import unittest
from unittest.mock import patch, mock_open

import random

from task_6 import LuckyTickets
from task_4 import File


class TestLuckyTickets(unittest.TestCase):
    """
    Test class for task_6
    """

    # check get_data method from File works properly
    @patch('builtins.open', mock_open(read_data='some text'))
    def test_file_get_data(self):
        file = File('path.txt')
        data = file.get_data
        self.assertEqual(data, 'some text')

    # check save_data method from File works properly
    def test_file_save_data(self):
        with patch('builtins.open', mock_open(), create=True) as f:
            file = File('test.txt')
            file.save_data('new text')
            f.assert_called_with('test.txt', 'w', encoding='UTF-8')
            f().write.assert_called_with('new text')

    # check get_moscow_lucky_tickets method from LuckyTickets works properly
    def test_get_moscow_lucky_tickets(self):
        mlt = []
        for _ in range(10):
            rnd = random.randint(1, 1000000)
            ticket = f'{rnd:06}'
            self.assertEqual(len(ticket), 6)

        tickets = ['111111', '020002', '003300']
        for ticket in tickets:
            if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
                mlt.append(ticket)
                self.assertIn(ticket, mlt)

    # check get_piter_lucky tickets method from LuckyTickets works properly
    def test_get_piter_lucky_tickets(self):
        plt = []
        for _ in range(10):
            rnd = random.randint(1, 1000000)
            ticket = f'{rnd:06}'
            self.assertEqual(len(ticket), 6)

        tickets = ['020011', '031202', '063300']
        for ticket in tickets:
            if sum([int(i) for i in ticket if int(i) % 2 == 0]) == \
                    sum([int(i) for i in ticket if int(i) % 2 != 0]):
                plt.append(ticket)
                self.assertIn(ticket, plt)

    # check input works properly
    @patch('builtins.input', return_value='Moscow')
    def test_input(self, mock_input):
        with patch('builtins.open', mock_open(read_data='Moscow')) as f:
            file = File('path.txt')
            fh = LuckyTickets(file)
            self.assertEqual(mock_input(), fh.file.get_data)