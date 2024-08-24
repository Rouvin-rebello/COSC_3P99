# function_3_test.py

import pytest
from Function_3_Source import Order, Item

# --------------------------------------------------------------------------------
# Tests for add_item method in Order class
# --------------------------------------------------------------------------------

def test_Order_add_item_to_empty():
    order = Order()
    first_item = Item('stuff', 12.34)
    order.add_item(first_item)
    assert len(order.items) == 1
    assert order.items[0] == first_item

def test_Order_add_item_to_existing():
    order = Order()
    item0 = Item('stuff', 12.34)
    item1 = Item('more', 9.99)
    order.add_item(item0)
    order.add_item(item1)
    assert len(order.items) == 2
    assert order.items[0] == item0
    assert order.items[1] == item1
