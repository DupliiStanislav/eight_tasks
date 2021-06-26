import unittest


class TestChessboard(unittest.TestCase):
    """
    Create test class for Chessboard
    """
    # Setup instance and args
    def setUp(self) -> None:
        from task_1 import Chessboard
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

    def setUp(self) -> None:
        from task_2 import Envelope
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

    def test_comparison(self):
        self.assertGreater(self.env2.width, self.env1.width)
        self.assertGreater(self.env2.length, self.env1.length)
        self.assertLess(self.env1.length, self.env2.length)
        self.assertLess(self.env1.length, self.env2.length)

        check = self.env1 - self.env2
        self.assertEqual(check, f'We can put {self.env1} into {self.env2}')


if __name__ == '__main__':
    unittest.main()