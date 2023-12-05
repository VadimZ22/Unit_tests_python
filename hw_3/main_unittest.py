import unittest
from main import (Tasks)


class Test(unittest.TestCase):
    def test_even_odd_number_test(self):
        self.assertTrue(Tasks.even_odd_number(4))

    def test_even_not_odd_number_test(self):
        self.assertFalse(Tasks.even_odd_number(5))

    def test_interval(self):
        self.assertTrue(Tasks.number_in_interval(50))

    def test_not_interval(self):
        self.assertFalse(Tasks.number_in_interval(25))

    def test_not_interval_up(self):
        self.assertFalse(Tasks.number_in_interval(100))
