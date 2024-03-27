import unittest
from calculator import add, subtract, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # 1 + 2 = 3
        self.assertEqual(add(0, 0), 0)   # 0 + 0 = 0
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 = 0

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)  # 3 - 2 = 1
        self.assertEqual(subtract(0, 0), 0)   # 0 - 0 = 0
        self.assertEqual(subtract(1, 2), -1)  # 1 - 2 = -1

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)  # 2 * 3 = 6
        self.assertEqual(multiply(0, 0), 0)  # 0 * 0 = 0
        self.assertEqual(multiply(6, 2), 12)  # 6 * 2 = 12

if __name__ == '__main__':
    unittest.main()
