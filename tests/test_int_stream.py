import unittest

from py3streams import IntStream


class TestStream(unittest.TestCase):

    def test_sum(self):
        value = IntStream(0, 10).sum()
        self.assertEqual(value, 45)




