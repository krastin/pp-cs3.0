import unittest

def find_min_max(values: list):
    """Print the minimum and maximum value from values.
    """
    min = None
    max = None
    for value in values:
        if max == None or value > max:
            max = value
        if min == None or value < min:
            min = value
    print('The minimum value is {0}'.format(min))
    print('The maximum value is {0}'.format(max))
    return (min, max)

class TestFindMinMax(unittest.TestCase):
    """ test find_min_max """

    def test1(self):
        argument = find_min_max([])
        expected = (None, None)
        self.assertEqual(argument, expected, "Empty result")

    def test2(self):
        argument = find_min_max([5])
        expected = (5, 5)
        self.assertEqual(argument, expected, "Single result")

    def test3(self):
        argument = find_min_max([-1, 5, 10])
        expected = (-1, 10)
        self.assertEqual(argument, expected, "Negative result")
    
    def test4(self):
        argument = find_min_max([-1, -3, -3, 20, 30])
        expected = (-3, 30)
        self.assertEqual(argument, expected, "Double result")

unittest.main()