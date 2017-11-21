import unittest

from fact import factorial

class Testfibonacci(unittest.TestCase):

    """
    Class contains test on the factorial function
    """

    def test_factorial_method_returns_correct_values(self):

        """
        Method tests whether factorial function returns correct values
        """

        result = factorial.factorial(3)
        self.assertEqual(6, result)


    def test_factorial_method_returns_1_for_0_input(self):

        """
        Method chacks whether factorial function returns 0 for input 1
        """

        result = factorial.factorial(0)
        self.assertEqual(1, result)

    def test_factorial_method_with_negative_input(self):

        """
        Method tests factorial funcion with negative integer input
        """

        self.assertRaises(RecursionError, factorial.factorial, -4)

    def test_factorial_method_for_non_integers(self):

        self.assertRaises(TypeError, factorial.factorial, 'Hello')

    def test_factorial_for_number_with_leading_plus_sign(self):

        result = factorial.factorial(+5)
        self.assertEqual(120,result)

    def test_factorial_for_number_with_leading_0(self):

        self.assertRaises(SyntaxError, factorial.factorial, 07)
