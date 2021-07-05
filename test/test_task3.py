import unittest
from task_3 import Triangle


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


if __name__ == '__main__':
    unittest.main()