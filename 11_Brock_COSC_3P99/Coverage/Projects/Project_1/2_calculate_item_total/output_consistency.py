# Output Consistency

def calculate_item_total(self):
    total = self.quantity * self.unit_price
    rounded = round(total, 2)  # Ensuring consistent output format
    return rounded
