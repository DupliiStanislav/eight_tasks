import unittest
from unittest.mock import patch, mock_open
from task_4 import File, FileHandler

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


if __name__ == '__main__':
    unittest.main()