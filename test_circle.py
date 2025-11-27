import unittest
from circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(2), math.pi * 4)

    def test_zero_area(self):
        self.assertAlmostEqual(area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)

    def test_zero_perimeter(self):
        self.assertAlmostEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()