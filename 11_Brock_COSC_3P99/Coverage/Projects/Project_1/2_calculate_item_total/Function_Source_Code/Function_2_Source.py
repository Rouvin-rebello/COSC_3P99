# function_1_source.py

class Item:
    def __init__(self, name, unit_price, quantity=1):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def calculate_item_total(self):
        total = self.quantity * self.unit_price
        rounded = round(total, 2)
        return rounded
