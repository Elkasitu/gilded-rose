import unittest

from gilded_rose import CommonItem, AgedItem, LegendaryItem, TimedItem, ConjuredItem, GildedRose

class GildedRoseTests(unittest.TestCase):
    def test_left_boundary(self):
        item = CommonItem("foo", 0, 0)
        gilded_rose = GildedRose([item])

        self.assertEqual(item.quality, 0)
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_common_item_decay(self):
        items = [
            CommonItem("foo", 1, 1),
            CommonItem("bar", 1, 10),
        ]
        gilded_rose = GildedRose(items)

        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[1].quality, 10)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 9)
        gilded_rose.update_quality()
        self.assertEqual(items[1].quality, 7)

    def test_aged_item_decay(self):
        items = [
            AgedItem("Aged Brie", 1, 0),
            AgedItem("Aged Brie", 0, 50),
        ]
        gilded_rose = GildedRose(items)

        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 50)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[1].quality, 50)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 3)

    def test_legendary_item_decay(self):
        items = [
            LegendaryItem("Sulfuras, Hand of Ragnaros", 0, 80),
            LegendaryItem("Sulfuras, Hand of Ragnaros", 1, 80),
        ]
        gilded_rose = GildedRose(items)

        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[1].quality, 80)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[1].quality, 80)

    def test_timed_item_decay(self):
        items = [
            TimedItem("Backstage passes to a TAFKAL80ETC concert", 11, 0),
            TimedItem("Backstage passes to a TAFKAL80ETC concert", 10, 0),
            TimedItem("Backstage passes to a TAFKAL80ETC concert", 5, 0),
            TimedItem("Backstage passes to a TAFKAL80ETC concert", 0, 50),
        ]
        gilded_rose = GildedRose(items)

        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 0)
        self.assertEqual(items[2].quality, 0)
        self.assertEqual(items[3].quality, 50)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[1].quality, 2)
        self.assertEqual(items[2].quality, 3)
        self.assertEqual(items[3].quality, 0)

    def test_conjured_decay(self):
        item = ConjuredItem("Master Sword", 1, 2)
        gilded_rose = GildedRose([item])

        self.assertEqual(item.quality, 2)
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
