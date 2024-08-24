# Combined_Test.py

import pytest
from unittest.mock import Mock
from Core_Functionality_Item import Item
from Core_Functionality_Order import Order

# --------------------------------------------------------------------------------
# Tests for Item Functionality
# --------------------------------------------------------------------------------

def test_Item_init():
    item = Item('stuff', 12.34, 3)
    assert item.name == 'stuff'
    assert item.unit_price == 12.34
    assert item.quantity == 3

def test_Item_calculate_item_total():
    item = Item('stuff', 12.34, 3)
    assert item.calculate_item_total() == 37.02

def test_Item_negative_price():
    with pytest.raises(ValueError):
        Item('stuff', -1, 1)

def test_Item_negative_quantity():
    with pytest.raises(ValueError):
        Item('stuff', 12.34, -1)

# --------------------------------------------------------------------------------
# Tests for Order Functionality
# --------------------------------------------------------------------------------

def test_Order_calculate_subtotal():
    order = Order()
    order.add_item(Item('stuff', 12.34, 2))
    assert order.calculate_subtotal() == 24.68

def test_Order_invalid_item():
    order = Order()
    with pytest.raises(TypeError):
        order.add_item("NotAnItem")

def test_Order_calculate_subtotal_for_multiple_items():
    order = Order()

    item0 = Mock()
    item0.calculate_item_total.return_value = 5
    order.add_item(item0)

    item1 = Mock()
    item1.calculate_item_total.return_value = 20
    order.add_item(item1)

    assert order.calculate_subtotal() == 25
