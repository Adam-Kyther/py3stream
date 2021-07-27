import unittest

from stream import IntStream


class TestStream(unittest.TestCase):

    def test_sum(self):
        value = IntStream(0, 10).sum()
        self.assertEquals(value, 45)




