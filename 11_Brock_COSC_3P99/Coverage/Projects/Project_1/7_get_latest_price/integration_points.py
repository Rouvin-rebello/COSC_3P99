import requests

def get_latest_price(item_id):
    endpoint = 'https://api.pandastore.com/getitem/' + str(item_id)
    response = requests.get(endpoint)
    price = response.json()['price']
    return price
