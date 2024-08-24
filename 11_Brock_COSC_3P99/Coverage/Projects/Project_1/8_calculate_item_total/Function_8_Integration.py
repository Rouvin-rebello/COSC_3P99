# Function_8_Integration.py

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
