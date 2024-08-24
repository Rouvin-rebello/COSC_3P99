# integration_points.py

from Core_Functionality import Order

class IntegrationPoints(Order):
    def calculate_order_total(self):
        subtotal = self.calculate_subtotal()
        total = self.calculate_total(subtotal, self.shipping, self.discount, self.tax_percent)
        return total
