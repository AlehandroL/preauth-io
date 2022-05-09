export class Item {
    name: string;
    sellIn: number;
    quality: number;

    constructor(name, sellIn, quality) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }
}


export class GildedRose {
    items: Array<Item>;

    constructor(items = [] as Array<Item>) {
        this.items = items;
    }


	modifyQuality(item, delta, max = 50, min = 0) {
		if (item.quality + delta > max) {
			item.quality = max
			return
		}
		if (item.quality + delta < min) {
			item.quality = min
			return
		}
		item.quality += delta
	}


	updateSellIn(item) {
		if (item.name == 'Sulfuras, Hand of Ragnaros') {
			return
		}
		item.sellIn -= 1
	}	
	

    updateQuality() {
		for (let item of this.items) {
			updateSellIn(item)
			if (item.name == 'Aged Brie') {
				if (item.sellIn < 0) {
					modifyQuality (item, 2)
					continue
				}
				modifyQuality(item, 1)
				continue
			}
			if (item.name == 'Backstage passes to a TAFKAL80ETC concert') {
				if (item.sellIn < 0){
					item.quality = 0
					continue
				}
				if (item.sellIn < 6){
					modifyQuality(item, 3)
					continue
				}
				if (item.sellIn < 11){
					modifyQuality(item, 2)
					continue
				}
				modifyQuality(item, 1)
				continue
			}
			if (item.name == 'Sulfuras, Hand of Ragnaros') {
				continue
			}
			if (item.name.includes("Conjured")) {
				if (item.sellIn < 0) {
					modifyQuality(item, -4)
					continue
				}
				modifyQuality(item, -2)
				continue
			}
			if (item.sellIn < 0) {
				modifyQuality(item, -2)
				continue
			}
			modifyQuality(item, -1)
		}
        return this.items;
    }
}
