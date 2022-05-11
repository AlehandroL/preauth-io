import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 3, 8), Item("Aged Brie", 4, 8), Item("Backstage passes to a TAFKAL80ETC concert", 12, 2), Item("Sulfuras, Hand of Ragnaros", 5, 80), Item("Conjured Sword", 4, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)
        self.assertEqual(9, items[1].quality)
        self.assertEqual(3, items[2].quality)
        self.assertEqual(80, items[3].quality)
        self.assertEqual(28, items[4].quality)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)
        self.assertEqual(15, items[1].quality)
        self.assertEqual(11, items[2].quality)
        self.assertEqual(80, items[3].quality)
        self.assertEqual(16, items[4].quality)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)
        self.assertEqual(23, items[1].quality)
        self.assertEqual(22, items[2].quality)
        self.assertEqual(80, items[3].quality)
        self.assertEqual(0, items[4].quality)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)
        self.assertEqual(31, items[1].quality)
        self.assertEqual(0, items[2].quality)
        self.assertEqual(80, items[3].quality)
        self.assertEqual(0, items[4].quality)
        
if __name__ == '__main__':
    unittest.main()