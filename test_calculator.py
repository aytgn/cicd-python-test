# test_calculator.py
import unittest
from calculator import bol, carp, cikar, topla

class TestCalculator(unittest.TestCase):
    def test_topla(self):
        # 2 ile 3'ü topladığımızda sonucun 5 olmasını bekliyoruz
        self.assertEqual(topla(2, 3), 5)
        
        # -1 ile 1'i topladığımızda sonucun 0 olmasını bekliyoruz
        self.assertEqual(topla(-1, 1), 0)

    def test_cikar(self):
        # 5'ten 3'ü çıkardığımızda sonucun 2 olmasını bekliyoruz
        self.assertEqual(cikar(5, 3), 2)

    def test_carp(self):
        # 4 ile 6'yı çarptığımızda sonucun 24 olmasını bekliyoruz
        self.assertEqual(carp(4, 6), 24)

    def test_bol(self):
        # 10'u 2'ye böldüğümüzde sonucun 5 olmasını bekliyoruz
        self.assertEqual(bol(10, 2), 5)

if __name__ == '__main__':
    unittest.main()