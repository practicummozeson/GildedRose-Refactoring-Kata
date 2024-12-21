# -*- coding: utf-8 -*-

class GildedRose(object):
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    FIXME = "fixme"
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        if item.sell_in == 0 and item.quality == 0:
            self.update_name(item)
            return

        if item.name == self.SULFURAS:
            return

        self.update_sell_in(item)

        if item.name == self.AGED_BRIE:
            self.update_aged_brie(item)
        elif item.name == self.BACKSTAGE:
            self.update_backstage_passes(item)
        else:
            self.update_normal_item(item)

        if item.sell_in < 0:
            self.handle_expired_item(item)

    def handle_expired_item(self, item):
        if item.quality > self.MIN_QUALITY:
            item.quality -= 1

    def update_name(self, item):
        item.name = self.FIXME

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_aged_brie(self, item):
        if item.quality < self.MAX_QUALITY:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.sell_in < 1:
            item.quality = 0
        elif item.sell_in < 6:
            item.quality += 2 if item.quality < self.MAX_QUALITY - 1 else 1
        elif item.sell_in < 11:
            item.quality += 1 if item.quality < self.MAX_QUALITY else 0

    def update_normal_item(self, item):
        if item.quality > self.MIN_QUALITY:
            item.quality -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
