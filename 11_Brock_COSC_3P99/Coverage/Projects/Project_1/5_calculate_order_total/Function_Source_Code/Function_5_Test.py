# Function_5_Test.py

import pytest
from unittest.mock import patch
from Function_5_Source import Order, calculate_total

def test_Order_calculate_order_total():
    order = Order(10, 5, 0.05)

    with patch.object(order, 'calculate_subtotal', return_value=100) as subtotal_mock:
        with patch('Function_5_Source.calculate_total', return_value=110.25) as total_mock:

            order_total = order.calculate_order_total()

            assert order_total == 110.25
            subtotal_mock.assert_called_once()
            total_mock.assert_called_once_with(100, 10, 5, 0.05)
