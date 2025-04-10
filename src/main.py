import unittest
import time
from src.main import add, subtract

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        time.sleep(2)
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        time.sleep(2)
        self.assertEqual(subtract(10, 4), 6)

    def test_add_negative(self):
        time.sleep(2)
        self.assertEqual(add(-1, -2), -3)

    def test_subtract_negative(self):
        time.sleep(2)
        self.assertEqual(subtract(-4, -2), -2)

    def test_mixed(self):
        time.sleep(2)
        self.assertEqual(add(5, -3), 2)

if __name__ == "__main__":
    unittest.main()
