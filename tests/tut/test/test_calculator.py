import unittest #import standard unittest module from library
from app.calculator import Calculator

class TddInPythonExample(unittest.TestCase):

    """

    This classs contains the different test cases for calculator.py

    """

    def test_calculator_add_method_returns_correct_result(self):
        """
        Method to test add function from calculator.py
        """
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()
