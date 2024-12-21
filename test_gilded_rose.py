# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.items = [Item("foo", 0, 0)]
        self.gilded_rose = GildedRose(self.items)

    def test_update_quality(self):
        self.gilded_rose.update_quality()
        self.assertEqual("fixme", self.items[0].name)
               
if __name__ == '__main__':
    unittest.main()
