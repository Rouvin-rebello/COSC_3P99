# output_consistency.py

from Core_Functionality import Order

class ConsistentOrder(Order):
    def calculate_total(self):
        total = sum(item.unit_price * item.quantity for item in self.items)
        return round(total, 2)
