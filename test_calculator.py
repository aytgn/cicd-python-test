# test_calculator.py
import unittest
from calculator import topla

class TestCalculator(unittest.TestCase):
    def test_topla(self):
        # 2 ile 3'ü topladığımızda sonucun 5 olmasını bekliyoruz
        self.assertEqual(topla(2, 3), 5)
        
        # -1 ile 1'i topladığımızda sonucun 0 olmasını bekliyoruz
        self.assertEqual(topla(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()