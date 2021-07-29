
from py3streams import Stream
import unittest


class TestStream(unittest.TestCase):

    def test_reverse(self):
        amount = Stream(["a", "b", "c", "d", None]).filter(lambda x: x is not None).count()
        self.assertEqual(amount, 4)

    def test_exists(self):
        amount = Stream(["a", "", [], None, "b", 2]).exists().count()
        self.assertEqual(amount, 3)

    def test_gt(self):
        elements = [1, 60, "100", 200, 300, 50]
        amount = Stream(elements).map(lambda x: int(x)).filter(lambda x: x <= 100).filter(lambda x: x > 50)
        self.assertEqual(amount.to_list(), [60, 100])

        # alternative with stream's functions
        amount = Stream(elements).map_to_int().le(100).gt(50)
        self.assertEqual(len(amount.operations()), 3)
        self.assertEqual(amount.to_list(), [60, 100])

        # Stream cannot be reused, generators are evaluated and they are empty.
        self.assertEqual(amount.count(), 0)

    def test_joining(self):
        elements = [1, 60, "100", 200, 300, 50]
        value = Stream(elements).map_to_int().le(50).map_to_str().joining("-")
        self.assertEqual(value, "1-50")
        value = Stream(elements).map_to_int().lt(50).map_to_str().joining("-")
        self.assertEqual(value, "1")

    def test_fmap(self):
        elements = [1, 2, [9, 8, 7]]
        value = Stream(elements).filter(lambda x: isinstance(x, list)).fmap(lambda x: Stream(x)).sum()
        self.assertEqual(value, 24)

    def test_merge_sub_lists(self):
        elements = [1, 2, [5, "5", 5], 3, "4", None, ["6"], ["7", 7]]
        sub_list = Stream(elements).only_list().fmap(lambda x: Stream(x)).to_list()
        self.assertEqual(sub_list, [5, "5", 5, "6", "7", 7])

        sub_list2 = Stream(elements).only_list().fmap(lambda x: Stream(x)).map_to_int().le(6).to_list()
        self.assertEqual(sub_list2, [5, 5, 5, 6])

    def test_only_digits(self):
        elements= ["a", "c", 1, 3, ["a", "b"], 4, "4.5", "4a"]
        values = Stream(elements).only_digits().to_list()
        self.assertEqual(values, [1, 3, 4, '4.5'])

