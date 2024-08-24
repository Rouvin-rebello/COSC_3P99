# Function_4_Test.py

import pytest
from Function_4_Source import Order, Item
from unittest.mock import Mock

def test_Order_calculate_subtotal_for_multiple_items():
    order = Order()

    item0 = Mock()
    item0.calculate_item_total.return_value = 5
    order.add_item(item0)

    item1 = Mock()
    item1.calculate_item_total.return_value = 20
    order.add_item(item1)

    assert order.calculate_subtotal() == 25

