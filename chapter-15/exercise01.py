from typing import List
import unittest

def double_preceding(values: List[float]) -> None:
    """Replace each item in the list with twice the value of the
    preceding item, and replace the first item with 0.
    >>> L = [1, 2, 3]
    >>> double_preceding(L)
    >>> L
    [0, 2, 4]
    """
    if values != []:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            #values[i] = 2 * temp
            #temp = values[i]
            double = 2 * temp
            temp = values[i]
            values[i] = double
        
class TestDoublePreceding(unittest.TestCase):
    """ Tests for double_preceding """

    def test_empty(self):
        """ Test an empty list """
        argument = []
        expected = []
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_one(self):
        """ Test an empty list """
        argument = [1]
        expected = [0]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one 0 item.")

    def test_zeroes(self):
        """ Test an empty list """
        argument = [0,0,0]
        expected = [0,0,0]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one 3 item.")

    def test_ones(self):
        """ Test an empty list """
        argument = [1,1,1]
        expected = [0,2,2]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one 3 item.")

    def test_positives(self):
        """ Test an empty list """
        argument = [1,2,3]
        expected = [0,2,4]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one 3 item.")

    def test_negatives(self):
        """ Test an empty list """
        argument = [-1,-2,-3]
        expected = [0,-2,-4]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one 3 item.")

    def test_random(self):
        """ Test an empty list """
        argument = [10,20,100]
        expected = [0,20,40]
        double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one 3 item.")

unittest.main()