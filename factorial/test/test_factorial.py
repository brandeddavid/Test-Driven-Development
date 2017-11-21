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
