import pytest
from item_core import Item
from unittest.mock import patch
from order_core import Order
import pytest
from total_boundary import calculate_total


def test_Item_init():
    item = Item('stuff', 12.34, 3)
    assert item.name == 'stuff'
    assert item.unit_price == 12.34
    assert item.quantity == 3

def test_Item_calculate_item_total():
    item = Item('stuff', 12.34, 3)
    assert item.calculate_item_total() == 37.02


def test_Order_calculate_order_total():
    order = Order(10, 5, 0.05)

    with patch.object(order, 'calculate_subtotal', return_value=100) as subtotal_mock:
        with patch('total_boundary.calculate_total', return_value=110.25) as total_mock:

            order_total = order.calculate_order_total()

            assert order_total == 110.25
            subtotal_mock.assert_called_once()
            total_mock.assert_called_once_with(100, 10, 5, 0.05)


def test_calculate_total():
    assert calculate_total(90, 10, 20, 0.05) == 84.00

def test_calculate_total_negatives():
    with pytest.raises(ValueError):
        calculate_total(-90, 10, 20, 0.05)
