# Function_Item.py

class Item:
    def __init__(self, name, unit_price, quantity=1):
        if unit_price < 0:
            raise ValueError("unit_price cannot be negative")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def calculate_item_total(self):
        total = self.quantity * self.unit_price
        rounded = round(total, 2)
        return rounded
