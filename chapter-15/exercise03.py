import unittest
from TestPrefixes.py import all_prefixes

class TestPrefixes(unittest.TestCase):
    """ Tests for all_prefixes """

    def test1(self):
        argument = all_prefixes("lead")
        expected = {"l", "le", "lea", "lead"}

        self.assertEqual(expected, argument, "OK result")

    def test2(self):
        argument = all_prefixes("")
        expected = {}
        self.assertEqual(expected, argument, "Empty result")

    def test3(self):
        argument = all_prefixes("'123'")
        expected = {"'", "'1", "'123", "'123"}
        self.assertEqual(expected, argument, "Quotes result")

    def test4(self):
        argument = all_prefixes("\0asd")
        expected = {"\0", "\0a", "\0as", "\0asd"}
        self.assertEqual(expected, argument, "Null terminator result")

unittest.main()