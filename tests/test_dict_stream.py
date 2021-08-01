from py3streams import Stream, DictStream

import unittest


class TestDictStream(unittest.TestCase):

    def test_fmap(self):
        elements = [1, "3", ["a", "b"], {"id":1, "values": [12, 34]}, {"id": 2, "values": [45, 67]}]
        values = Stream(elements).filter(lambda x: isinstance(x, dict)).fmap(lambda x: DictStream(x)).filter(lambda entry: entry[0] == "values").map(lambda entry: entry[1]).fmap(lambda x: Stream(x)).to_list()
        self.assertEqual(values, [12, 34, 45, 67])

        ids = Stream(elements).filter(lambda x: isinstance(x, dict)).fmap(lambda x: DictStream(x)).filter(lambda e: e[0] == "id").map(lambda e: e[1]).to_list()
        self.assertEqual(ids, [1, 2])

        ids2 = Stream(elements).only_dict().fmap(lambda x: DictStream(x)).filter(lambda e: e[0] == "id").map(lambda e: e[1]).to_list()
        self.assertEqual(ids2, [1, 2])

    def test_stream_fmap(self):
        elements = {"id": 1, "values": [[1,2,3], [5,7]], "test": True}
        result = DictStream(elements).values().only_list().fmap(lambda x: Stream(x)).fmap(lambda x: Stream(x)).to_list()
        self.assertEqual(result, [1, 2, 3, 5, 7])

