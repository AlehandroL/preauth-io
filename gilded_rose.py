from abc import abstractclassmethod

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            inventory_item = Inventory_item.create(item)
            inventory_item.update_item_quality()


class Item():
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Inventory_item:
    def __init__(self, item: Item):
        self.item = item

    @staticmethod
    def create(item) -> Item:
        SULFURAS = 'Sulfuras, Hand of Ragnaros'
        TICKET = 'Backstage passes to a TAFKAL80ETC concert'
        BRIE = 'Aged Brie'
        CONJURED = 'conjured'
        if item.name == SULFURAS:
            return Legendary_item(item)
        if item.name == TICKET:
            return Expirable_item(item)
        if item.name == BRIE:
            return Aging_item(item)
        if CONJURED in item.name.lower():
            return Conjured_item(item)
        return Normal_item(item)
    
    def update_item_quality(self):
        self.update_sellIn()
        if self.is_expired():
            self.handle_expired()
        else:
            self.handle_not_expired()

    def is_expired(self) -> bool:
        if self.item.sell_in == 0:
            return True
        return False

    def update_sellIn(self):
        if not self.is_expired():
            self.item.sell_in -= 1

    def increase_quality(self, n: int):
        if self.item.quality + n > 50:
            self.item.quality = 50
        else:
            self.item.quality += n
    
    def decrease_quality(self, n: int):
        if self.item.quality - n < 0:
            self.item.quality = 0
        else:
            self.item.quality -= n

    def set_quality(self, n: int):
        self.item.quality = n

    @abstractclassmethod
    def handle_expired(self):
        pass

    @abstractclassmethod
    def handle_not_expired(self):
        pass

class Legendary_item(Inventory_item):
    def handle_expired(self):
        pass

    def handle_not_expired(self):
        pass

class Expirable_item(Inventory_item):
    def handle_expired(self):
        self.set_quality(0)

    def handle_not_expired(self):
        if self.item.sell_in < 6:
            self.increase_quality(3)
            return
        if self.item.sell_in < 11:
            self.increase_quality(2)
            return
        self.increase_quality(1)

class Aging_item(Inventory_item):
    def handle_expired(self):
        self.increase_quality(2)
    
    def handle_not_expired(self):
        self.increase_quality(1)

class Normal_item(Inventory_item):
    def handle_expired(self):
        self.decrease_quality(2)
    
    def handle_not_expired(self):
        self.decrease_quality(1)

class Conjured_item(Inventory_item):
    def handle_expired(self):
        self.decrease_quality(4)
    
    def handle_not_expired(self):
        self.decrease_quality(2)


