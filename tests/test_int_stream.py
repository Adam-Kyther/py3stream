import unittest

from py3streams import IntStream


class TestStream(unittest.TestCase):

    def test_sum(self):
        value = IntStream(0, 10).sum()
        self.assertEqual(value, 45)

    def test_count(self):
        # amount = IntStream(0, 10, 2).filter(lambda x: x < 5).count()
        amount = IntStream(0, 10, 2).lt(5).count()
        self.assertEqual(amount, 3)

    def test_convert_to_list(self):
        result = IntStream(0, 10).even().to_list()
        self.assertEqual(result, [0, 2, 4, 6, 8])

    def test_reverse(self):
        result = IntStream(0, 10).odd().reverse()
        self.assertEqual(list(result), [9, 7, 5, 3, 1])

