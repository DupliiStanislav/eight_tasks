import unittest
from task_2 import Envelope

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


if __name__ == '__main__':
    unittest.main()