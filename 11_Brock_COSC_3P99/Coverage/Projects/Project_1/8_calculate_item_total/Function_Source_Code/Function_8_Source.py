import requests

# --------------------------------------------------------------------------------
# Class: Item
# --------------------------------------------------------------------------------

class Item:
    def __init__(self, name, unit_price, quantity=1):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def calculate_item_total(self):
        total = self.quantity * self.unit_price
        rounded = round(total, 2)
        return rounded


# --------------------------------------------------------------------------------
# Class: DynamicallyPricedItem
# --------------------------------------------------------------------------------

class DynamicallyPricedItem:
    def __init__(self, id, quantity=1):
        self.id = id
        self.quantity = quantity

    def get_latest_price(self):
        endpoint = 'https://api.pandastore.com/getitem/' + str(self.id)
        response = requests.get(endpoint)
        price = response.json()['price']
        return price

    def calculate_item_total(self):
        total = self.quantity * self.get_latest_price()
        rounded = round(total, 2)
        return rounded
