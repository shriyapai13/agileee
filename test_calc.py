import unittest
import calc

class TestCalc(unittest.TestCase):

    # Testing the add function
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)  # Testing with negative numbers
        self.assertEqual(calc.add(2.5, 3.5), 6.0)  # Testing with floats
        self.assertEqual(calc.add(0, 0), 0)  # Testing with zeros

    # Testing the subtract function
    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(-1, 1), -2)  # Testing with negative numbers
        self.assertEqual(calc.subtract(2.5, 1.5), 1.0)  # Testing with floats
        self.assertEqual(calc.subtract(0, 0), 0)  # Testing with zeros

    # Additional test to ensure that subtracting zero doesn't change the result
    def test_subtract_zero(self):
        self.assertEqual(calc.subtract(5, 0), 5)
        self.assertEqual(calc.subtract(0, 0), 0)

    # Additional test for adding zero (this is more about ensuring the function handles zero correctly)
    def test_add_zero(self):
        self.assertEqual(calc.add(5, 0), 5)
        self.assertEqual(calc.add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
