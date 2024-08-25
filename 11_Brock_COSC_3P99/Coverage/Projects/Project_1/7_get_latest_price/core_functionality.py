from integration_points import get_latest_price

class DynamicallyPricedItem:
    def __init__(self, id, quantity=1):
        self.id = id
        self.quantity = quantity

    def calculate_item_total(self):
        total = self.quantity * get_latest_price(self.id)
        rounded = round(total, 2)
        return rounded
