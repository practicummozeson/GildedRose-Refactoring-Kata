# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

DEFAULT_DAYS = 2

def main(days):
    items = [
        Item(name="foo", sell_in=0, quality=0),
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]

    for day in range(days):
        print_day_summary(day, items)
        GildedRose(items).update_quality()

def print_day_summary(day, items):
    print("-------- day %s --------" % day)
    print("name, sellIn, quality")
    for item in items:
        print(item)
    print("")

if __name__ == "__main__":
    days = DEFAULT_DAYS
    import sys
    if len(sys.argv) > 1:
        days = max(0, int(sys.argv[1])) + 1
    main(days)