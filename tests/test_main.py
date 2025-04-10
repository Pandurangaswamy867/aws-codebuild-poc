import unittest
from src.main import add, subtract

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

if __name__ == "__main__":
    unittest.main()
