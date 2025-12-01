import unittest
import calculator.calculator as calc

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 2), 3)
        self.assertEqual(calc.subtract(2, 5), -3)
        self.assertEqual(calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-1, 5), -5)
        self.assertEqual(calc.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(6, 2), 3)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(10, -2), -5)
        self.assertEqual(calc.divide(5, 0), "Error! Cannot divide by zero.")

if __name__ == '__main__':
    unittest.main()