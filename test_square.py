import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area_int(self):
        self.assertEqual(area(4), 16)

    def test_zero_area(self):
        self.assertEqual(area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_perimeter_int(self):
        self.assertEqual(perimeter(3), 12)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(1.2), 4.8)

if __name__ == '__main__':
    unittest.main()