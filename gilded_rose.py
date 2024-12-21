# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.quality == 0 and item.sell_in == 0:
                self.update_name(item) 
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            self.update_sell_in(item)

            update_strategy = {
                "Aged Brie": self.update_aged_brie,
                "Backstage passes to a TAFKAL80ETC concert": self.update_backstage_passes,
            }

            update_func = update_strategy.get(item.name, self.update_normal_item)
            update_func(item)

    def update_name(self, item):
        item.name = "fixme"

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.sell_in < 1:
            item.quality = 0
        elif item.sell_in < 6:
            item.quality += 2 if item.quality < 49 else 1
        elif item.sell_in < 11:
            item.quality += 1 if item.quality < 50 else 0

    def update_normal_item(self, item):
        if item.quality > 0:
            item.quality -= 1
           
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)