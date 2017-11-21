import unittest

from fact import factorial

class Testfibonacci(unittest.TestCase):

    """
    Class contains test on the factorial function
    """

    def test_fact_method_returns_correct_values(self):

        result = factorial.factorial(3)
        self.assertEqual(6, result)
