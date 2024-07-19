import requests

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