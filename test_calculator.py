import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate(6, "*", 3), 18)
        self.assertEqual(calculate(10, "/", 4), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(5, "/", 0)

    def test_sqrt(self):
        self.assertEqual(calculate(16, "sqrt", 0), 4)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            calculate(-4, "sqrt", 0)

    def test_sin(self):
        self.assertEqual(calculate(30, "sin", 0), 0.5)
        self.assertEqual(calculate(180, "sin", 0), 0)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, "?", 1)

if __name__ == "__main__":
    unittest.main()