import unittest
from calculator import bol, carp, cikar, topla

class TestCalculator(unittest.TestCase):
    def test_topla(self):
        self.assertEqual(topla(2, 3), 5)
        self.assertEqual(topla(-1, 1), 0)

    def test_cikar(self):
        self.assertEqual(cikar(5, 3), 2)

    def test_carp(self):
        self.assertEqual(carp(4, 6), 24)

    def test_bol(self):
        self.assertEqual(bol(10, 2), 5)

if __name__ == '__main__':
    unittest.main()