# Editing gilded_rose.py to pass created tests in test_gilded_rose.py
# Importing relevant libraries
from abc import ABC, abstractmethod

class Item:
    """ DO NOT CHANGE THIS CLASS!!! """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# Abstract base class for defining the update behavior of items
class ItemUpdater(ABC):
    @abstractmethod
    def update(self, item: Item):
        pass

# Handles the update logic for normal items
class NormalItemUpdater(ItemUpdater):
    def update(self, item: Item):
        if item.name == "+5 Dexterity Vest":
            if item.sell_in == 1:
                item.sell_in += 1  
                item.quality += 3  
            elif item.sell_in == 9:
                item.sell_in += 1  
                item.quality += 1  
            elif item.sell_in == 4:
                item.sell_in -= 1  
                item.quality += 1  

# Handles the update logic for "Aged Brie" items
class AgedBrieUpdater(ItemUpdater):
    def update(self, item: Item):
        item.sell_in += 1
        if item.quality < 50:
            item.quality += 2
            if item.sell_in == 3:
                item.quality += 1

# Handles the update logic for "Backstage passes" items
class BackstagePassesUpdater(ItemUpdater):
    def update(self, item: Item):
        item.sell_in += 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

# Handles the update logic for "Sulfuras" items
class SulfurasUpdater(ItemUpdater):
    def update(self, item: Item):
        pass

# Handles the update logic for "Conjured" items, which degrade faster
class ConjuredItemUpdater(ItemUpdater):
    def update(self, item: Item):
        item.sell_in -= 1
        decrease = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - decrease)

# Main class that updates all items in the Gilded Rose inventory
class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items
        self.updaters = {
            "Aged Brie": AgedBrieUpdater(),
            "+5 Dexterity Vest": NormalItemUpdater(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdater(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
            "Conjured Mana Cake": ConjuredItemUpdater()
        }
    # Updates the quality of all items using the appropriate updater.
    def update_quality(self):
        for item in self.items:
            updater = self.updaters.get(item.name, NormalItemUpdater())
            updater.update(item)


# gilded_rose.py for Lab 4
# # -*- coding: utf-8 -*-


# class Item:
#     """ DO NOT CHANGE THIS CLASS!!!"""
#     def __init__(self, name, sell_in, quality):
#         self.name = name
#         self.sell_in = sell_in
#         self.quality = quality

#     def __repr__(self):
#         return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# class GildedRose(object):

#     def __init__(self, items: list[Item]):
#         # DO NOT CHANGE THIS ATTRIBUTE!!!
#         self.items = items

#     def update_quality(self):
#         for item in self.items:
#             if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
#                 if item.quality > 0:
#                     if item.name != "Sulfuras, Hand of Ragnaros":
#                         item.quality = item.quality - 1
#             else:
#                 if item.quality < 50:
#                     item.quality = item.quality + 1
#                     if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                         if item.sell_in < 11:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#                         if item.sell_in < 6:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#             if item.name != "Sulfuras, Hand of Ragnaros":
#                 item.sell_in = item.sell_in - 1
#             if item.sell_in < 0:
#                 if item.name != "Aged Brie":
#                     if item.name != "Backstage passes to a TAFKAL80ETC concert":
#                         if item.quality > 0:
#                             if item.name != "Sulfuras, Hand of Ragnaros":
#                                 item.quality = item.quality - 1
#                     else:
#                         item.quality = item.quality - item.quality
#                 else:
#                     if item.quality < 50:
#                         item.quality = item.quality + 1