Solutions for preauth games (in python)

For game_01:

Algorithm:
    Initialize an empty dictionary or hashable object
    Loop over the input array
    For each item in the array, calculate the complement (complement = N - (item value))
    Use "get" on the dictionary object using key = complement:
        if it finds the key, means that the complement was a previous item in the array, so we return the touple [complement, item value]
        if it doesn't find it, we insert a new touple in the dictionary object consisting in the {(item value): complement}
    
Time & space complexity (O(n) | O(n)):
    Using "get" on a hashable object has a time complexity of O(1), and traversing an array of length n is O(n) -> Time complexity = O(n)
    The dictionary or hashable object created is O(n) -> Space complexity = O(n)


For gilded_rose:

I found a python version of the kata online in order to feel more comfortable lenguage-wise.
To avoid changing the Item class, I wrote an Inventory_item class that has an Item inside. It includes some auxiliary methods to change Item's atributes and also a couple of static and abstract methods:
    Inventory_item.create: an static method which creates an object of a class that inherits from Inventory_item depending on the Item's name (e.g. for an Item named 'Sulfuras, Hand of Ragnaros', Create would create a Legendary_item object).
    Inventory_item.handle_expired: an abstract method that must be implemented by child classes.
    Inventory_item.handle_not_expired: an abstract method that must be implemented by child classes.
    Inventory_item.update_item_quality: a method that first updates the sell_in value of the subyacent Item, checks if the Item has expired and then proceeds depending on the result with one of the previous abstract methods (handle_expired, handle_not_expired)

I included a test file for gilded_rose with assertions on every type of object, in all of the ranges that variations change.