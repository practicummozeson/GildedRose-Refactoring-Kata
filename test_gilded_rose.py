# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

FIXME_NAME = "fixme"

class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.items = [
            Item("foo", 0, 0),
            Item("+5 Dexterity Vest", 10, 20),
            Item("Aged Brie", 2, 0),
            Item("Elixir of the Mongoose", 5, 7),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Sulfuras, Hand of Ragnaros", -1, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            Item("Conjured Mana Cake", 3, 6),
        ]
        
        self.gilded_rose = GildedRose(self.items)

    def test_update_quality(self):
        self.gilded_rose.update_quality()
        self.assertEqual(FIXME_NAME, self.items[0].name)

        self.assertEqual(9, self.items[1].sell_in)
        self.assertEqual(19, self.items[1].quality)

        self.assertEqual(1, self.items[2].sell_in)
        self.assertEqual(1, self.items[2].quality)

        self.assertEqual(4, self.items[3].sell_in)
        self.assertEqual(6, self.items[3].quality)

        self.assertEqual(0, self.items[4].sell_in)
        self.assertEqual(80, self.items[4].quality)

        self.assertEqual(-1, self.items[5].sell_in)
        self.assertEqual(80, self.items[5].quality)

        self.assertEqual(14, self.items[6].sell_in)
        self.assertEqual(20, self.items[6].quality)

        self.assertEqual(9, self.items[7].sell_in)
        self.assertEqual(50, self.items[7].quality)

        self.assertEqual(4, self.items[8].sell_in)
        self.assertEqual(50, self.items[8].quality)

        self.assertEqual(2, self.items[9].sell_in)
        self.assertEqual(5, self.items[9].quality)
        
if __name__ == '__main__':
    unittest.main()
