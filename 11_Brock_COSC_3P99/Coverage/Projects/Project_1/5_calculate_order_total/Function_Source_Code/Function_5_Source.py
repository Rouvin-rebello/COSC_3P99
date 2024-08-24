# Function_5_Source.py

def calculate_total(subtotal, shipping, discount, tax_percent):
    if subtotal < 0:
        raise ValueError('subtotal cannot be negative')
    if shipping < 0:
        raise ValueError('shipping cannot be negative')
    if discount < 0:
        raise ValueError('discount cannot be negative')
    if tax_percent < 0:
        raise ValueError('tax_percent cannot be negative')

    amount = subtotal + shipping - discount
    if amount < 0:
        total = 0
    else:
        total = amount * (1 + tax_percent)

    rounded = round(total, 2)
    return rounded


class Item:
    def __init__(self, name, unit_price, quantity=1):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def calculate_item_total(self):
        total = self.quantity * self.unit_price
        rounded = round(total, 2)
        return rounded


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
