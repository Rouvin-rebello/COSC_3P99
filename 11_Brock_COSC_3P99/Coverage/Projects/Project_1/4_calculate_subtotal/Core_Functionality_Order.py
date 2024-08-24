# Function_Order.py

from Core_Functionality_Item import Item

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, Item):
            raise TypeError("Only Item objects can be added")
        self.items.append(item)

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.calculate_item_total()
        return subtotal
