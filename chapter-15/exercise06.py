import unittest

from typing import List

def average(values: List[float]) -> float:
    """Return the average of the numbers in values. Some items in values are
    None, and they are not counted toward the average.
    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """
    count = 0 # The number of values seen so far.
    total = 0 # The sum of the values seen so far.
    for value in values:
        if value is not None:
            total += value
            count += 1
    if count == 0:
        return 0
    else:
        return total / count

class TestAverage(unittest.TestCase):
    """ test average() """

    def test1(self):
        argument = average([20, 30])
        expected = 25.0
        self.assertEqual(argument, expected, "Simple Result")

    def test2(self):
        argument = average([None, 20, 30])
        expected = 25.0
        self.assertEqual(argument, expected, "None-item Result")

    def test3(self):
        argument = average([None, 20, 30, None])
        expected = 25.0
        self.assertEqual(argument, expected, "None-items Result")

    def test4(self):
        argument = average([None, None, None])
        expected = 0
        self.assertEqual(argument, expected, "Nones Result")
    
unittest.main()