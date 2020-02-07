# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class CommonItem(Item):
    def update(self):
        self._update_quality()
        self._update_sell_in()

    @property
    def delta(self):
        return -1 if self.sell_in else -2

    def _update_quality(self):
        new_quality = self.quality + self.delta
        if new_quality > 0:
            if new_quality < 50:
                self.quality = new_quality
            else:
                self.quality = 50
        else:
            self.quality = 0

    def _update_sell_in(self):
        self.sell_in -= 1


class AgedItem(CommonItem):
    @property
    def delta(self):
        return 1 if self.sell_in else 2


class LegendaryItem(CommonItem):
    def _update_quality(self):
        pass


class TimedItem(CommonItem):
    @property
    def delta(self):
        if self.sell_in > 10:
            return 1
        elif self.sell_in > 5:
            return 2
        elif self.sell_in > 0:
            return 3
        else:
            return float('-inf')


class ConjuredItem(CommonItem):
    @property
    def delta(self):
        return super().delta * 2
