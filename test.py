import unittest
from mock import patch, mock_open, MagicMock, Mock

import random
import tkinter as tk

from task_1 import Chessboard
from task_2 import Envelope
from task_3 import Triangle
from task_4 import File, FileHandler, FILE_PATH_MSG
from task_5 import NumToString, NUMBERS, THOUSANDS, MILLIONS, GUI


class TestChessboard(unittest.TestCase):
    """
    tests for task_1
    """
    # Setup instance and args
    def setUp(self) -> None:
        self.chessboard = Chessboard(3, 3)

    # test number of args
    def test_number_of_args(self):
        self.assertEqual(2, len(self.chessboard.__dict__))

    # test type of args
    def test_int_args(self):
        self.assertIsInstance(self.chessboard.rows, int)
        self.assertIsInstance(self.chessboard.cols, int)

    # test list append in create board func
    def test_create_board(self):
        self.chessboard.create_board()
        self.assertIn(['*' for i in range(self.chessboard.rows)], self.chessboard.create_board())

    # test print of chessboard
    def test_proper_print(self):
        show = f' * * *\n* * *\n * * *'
        self.assertEqual(self.chessboard.show_board(), print(show))


class TestEnvelope(unittest.TestCase):
    """
    tests for task_2
    """
    def setUp(self) -> None:
        self.env1 = Envelope(3, 3)
        self.env2 = Envelope(6, 7)

        # test number of args
    def test_number_of_args(self):
        self.assertEqual(2, len(self.env1.__dict__))
        self.assertEqual(2, len(self.env2.__dict__))

    # test type of args
    def test_int_args(self):
        self.assertIsInstance(self.env1.width, int)
        self.assertIsInstance(self.env1.length, int)
        self.assertIsInstance(self.env2.width, int)
        self.assertIsInstance(self.env2.length, int)

    # check if we can properly compare two envelopes
    def test_comparison(self):
        self.assertGreater(self.env2.width, self.env1.width)
        self.assertGreater(self.env2.length, self.env1.length)
        self.assertLess(self.env1.length, self.env2.length)
        self.assertLess(self.env1.length, self.env2.length)

        check = self.env1 - self.env2
        self.assertEqual(check, f'We can put {self.env1} into {self.env2}')


# Test for task_3
class TestTriangle(unittest.TestCase):
    """
    tests for task_3
    """
    def setUp(self) -> None:

        self.tr1 = Triangle('one', 3, 4, 5)
        self.tr2 = Triangle('two', 22, 23, 20)
        self.tr3 = Triangle('three', 10, 9, 12)

    # check if we can make such triangle
    def test_is_exist(self):
        for tr in (self.tr1, self.tr2, self.tr3):
            self.assertGreater((tr.side1 + tr.side2), tr.side3)
            self.assertGreater((tr.side1 + tr.side2), tr.side3)
            self.assertGreater((tr.side1 + tr.side2), tr.side3)
            self.assertGreater((tr.side1 + tr.side3), tr.side2)
            self.assertGreater((tr.side1 + tr.side3), tr.side2)
            self.assertGreater((tr.side1 + tr.side3), tr.side2)
            self.assertGreater((tr.side2 + tr.side3), tr.side1)
            self.assertGreater((tr.side2 + tr.side3), tr.side1)
            self.assertGreater((tr.side2 + tr.side3), tr.side1)

    # check that we get proper square size
    def test_get_square(self):
        self.assertEqual(6, self.tr1.get_square)
        self.assertEqual(float(201.30434048971722), self.tr2.get_square)
        self.assertEqual(float(44.039045175843675), self.tr3.get_square)

    # check that add to dict works properly
    def test_in_dict(self):
        triangles_dct = {self.tr1.name: self.tr1.get_square}
        self.assertIn(self.tr1.get_square, triangles_dct.values())
        self.assertIn(self.tr1.name, triangles_dct)


class TestFileData(unittest.TestCase):
    """
    tests for task_4
    """
    # test if we can save data
    def test_save_data(self):
        m = mock_open()
        with patch('builtins.open',  m, create=True) as f:
            file = File('test.txt')
            file.save_data('next text')
            f.assert_called_with('test.txt', 'w', encoding='UTF-8')
            handle = f()
            handle.write.assert_called_with('next text')

    # test if method read data
    def test_get_data(self):
        with patch('builtins.open', mock_open(read_data='text')) as f:
            file = File('test.txt')
            result = file.get_data
            assert result == 'text'

    # test method for count substrings
    def test_counter_for_string(self):
        with patch('builtins.open', mock_open(read_data='text')) as f:
            file = File('test.txt')
            result = file.get_data
            fh = FileHandler(result, 'text')
            res = fh.counter_for_string()
            self.assertEqual(1, res)
            self.assertNotEqual(0, res)

    # test method to change substrings
    def test_change_string(self):
        with patch('builtins.open', mock_open(read_data='text'), create=True) as f:
            file = File('test.txt')
            fh = FileHandler(file.get_data, 't', 'n')
            res = fh.change_string()
            assert res == 'nexn'

    # test if we ask for save we get read and save our data
    @patch('builtins.input', return_value='yes')
    def test_ask_for_save_data(self, mock_input):
        with patch('builtins.open', mock_open(read_data='text')) as f:
            file = File('test.txt')
            fh = FileHandler(file.get_data, 't', 'n')
            res = fh.change_string()
            assert res == 'nexn'
            with patch('builtins.open', mock_open(), create=True) as w:
                fh.ask_save_new_data(file)
                assert input() == 'yes'
                w.assert_called_with('test.txt', 'w', encoding='UTF-8')
                handle = w()
                handle.write.assert_called_with('nexn')
                print(w.mock_calls)


class TestNumToString(unittest.TestCase):
    """
    test for task 5
    """
    # setup instancies and root
    def setUp(self) -> None:
        self.root = tk.Tk()
        self.events()
        self.ntm1 = NumToString(1)
        self.ntm2 = NumToString(1001)
        self.ntm3 = NumToString(1020001)

    # teardown to shout up the root and events
    def tearDown(self) -> None:
        if self.root:
            self.root.destroy()
            self.events()

    # events mask
    def events(self):
        while self.root.dooneevent(tk._tkinter.ALL_EVENTS | tk._tkinter.DONT_WAIT):
            pass

    # test entry method for GUI
    def test_entry_tk(self):
        gui = GUI(self.root)

        self.events()
        gui.inputs.focus_set()
        gui.inputs.insert(tk.END, '152')
        gui.inputs.event_generate('<Return>')
        self.events()
        self.assertEqual('152', gui.inputs.get())
        num_to_string = NumToString(int(gui.inputs.get()))
        self.assertEqual(num_to_string.get_string(), 'сто пятьдесят два')

    # test get name method for nums
    def test_get_name(self):
        for i in range(10):
            rnd_num = random.randint(1, 20)
            if rnd_num > 2:
                self.assertEqual(self.ntm1.get_name(rnd_num), NUMBERS[rnd_num])
            else:
                self.assertEqual(self.ntm1.get_name(rnd_num), NUMBERS[rnd_num][0])

        self.assertEqual(self.ntm2.get_name(999), 'девятьсот девяносто девять')
        self.assertEqual(self.ntm2.get_name(102), 'сто два')

    # get proper name for thousands and millions
    def test_get_proper_name(self):

        self.assertEqual(self.ntm2.get_proper_name, 'тысяча')
        self.assertEqual(self.ntm3.get_proper_name[1], 'миллион')




if __name__ == '__main__':
    unittest.main()
