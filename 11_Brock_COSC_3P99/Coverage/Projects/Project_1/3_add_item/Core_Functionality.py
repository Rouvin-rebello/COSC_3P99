# core_functionality.py

class Item:
    def __init__(self, name, unit_price, quantity=1):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

class Order:
    def __init__(self, shipping=0, discount=0, tax_percent=0):
        self.items = []
        self.shipping = shipping
        self.discount = discount
        self.tax_percent = tax_percent

    def add_item(self, item):
        self.items.append(item)
