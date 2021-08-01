from py3streams import Optional

import unittest


class TestOptional(unittest.TestCase):

    def test_get(self):
        opt = Optional.empty()
        self.assertEqual(opt.get(), None)

    def test_get_or_else(self):
        content = {
            'id': 0, 'value': 'first-1'
        }
        opt = Optional.of(content)
        self.assertEqual(opt.get().get('id'), 0)
        self.assertEqual(opt.get(), content)

        opt = Optional.of(None)
        self.assertEqual(opt.get_or_else("none"), "none")

