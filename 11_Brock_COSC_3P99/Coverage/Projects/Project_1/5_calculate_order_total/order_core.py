from item_core import Item
from total_boundary import calculate_total

class Order:
    def __init__(self, shipping=0, discount=0, tax_percent=0):
        self.items = []
        self.shipping = shipping
        self.discount = discount
        self.tax_percent = tax_percent

    def add_item(self, item):
        self.items.append(item)

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.calculate_item_total()
        return subtotal

    def calculate_order_total(self):
        subtotal = self.calculate_subtotal()
        total = calculate_total(
            subtotal, self.shipping, self.discount, self.tax_percent)
        return total
