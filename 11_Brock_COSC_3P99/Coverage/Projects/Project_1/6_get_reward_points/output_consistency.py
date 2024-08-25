# output_consistency.py

from Core_Functionality import Order

class OutputConsistency(Order):
    def calculate_total(self, subtotal, shipping, discount, tax_percent):
        amount = subtotal + shipping - discount
        if amount < 0:
            total = 0
        else:
            total = amount * (1 + tax_percent)
        rounded = round(total, 2)
        return rounded
