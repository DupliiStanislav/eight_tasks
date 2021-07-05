import unittest

from task_1 import Chessboard


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


if __name__ == '__main__':
    unittest.main()