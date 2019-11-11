import is_sorted from TestSorting.py

import unittest

class TestIsSorted(unittest.TestCase):
    """ test for is_sorted
    is_sorted - takes a list of integers as input and
    returns True if they are sorted in nondecreasing order
    """

    def test1(self):
        argument = is_sorted([])
        expected = True
        self.assertEqual(expected, argument, "Empty result")

    def test2(self):
        argument = is_sorted([1])
        expected = True
        self.assertEqual(expected, argument, "Single item result")

    def test3(self):
        argument = is_sorted([1, 1, 2, 3, 4])
        expected = True
        self.assertEqual(expected, argument, "Doubles result")

    def test4(self):
        argument = [-1, 1, 4, 6]
        expected = True
        is_sorted(argument)
        self.assertEqual(expected, argument, "Negatives result")

unittest.main()