# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        expected = [Item(vest, 2, 5), Item(vest, 10, 20), Item(vest, 3, 7)]
        actual = items
        self.assertEqual(str(actual), str(expected))  # This test should fail initially

    def test_aged_brie_increases_in_quality(self):
        aged_brie = "Aged Brie"
        items = [Item(aged_brie, 2, 0), Item(aged_brie, 5, 48)]
        gr = GildedRose(items)

        gr.update_quality()

        expected = [Item(aged_brie, 3, 3), Item(aged_brie, 6, 50)]
        actual = items
        self.assertEqual(str(actual), str(expected))  

    def test_conjured_items_degrade_twice_as_fast(self):
        conjured_item = "Conjured Mana Cake"
        items = [Item(conjured_item, 3, 6), Item(conjured_item, 1, 8)]
        gr = GildedRose(items)

        gr.update_quality()

        expected = [Item(conjured_item, 2, 4), Item(conjured_item, 0, 6)]
        actual = items
        self.assertEqual(str(actual), str(expected))  

if __name__ == '__main__':
    unittest.main()
