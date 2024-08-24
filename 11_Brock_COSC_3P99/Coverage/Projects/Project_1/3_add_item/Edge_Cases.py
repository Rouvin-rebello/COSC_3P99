# item_core

from Core_Functionality import Order, Item

def check_item_quantity(item):
    if item.quantity < 1:
        raise ValueError("Quantity must be at least 1")

class OrderWithBoundaryChecks(Order):
    def add_item(self, item):
        check_item_quantity(item)
        super().add_item(item)
