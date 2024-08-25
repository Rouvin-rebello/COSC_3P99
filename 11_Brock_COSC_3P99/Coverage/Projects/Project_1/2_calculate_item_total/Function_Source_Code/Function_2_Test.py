# function_1_test.py

import pytest
from Function_2_Source import Item

# --------------------------------------------------------------------------------
# Tests for Item
# --------------------------------------------------------------------------------

def test_Item_init():
    item = Item('stuff', 12.34, 3)
    assert item.name == 'stuff'
    assert item.unit_price == 12.34
    assert item.quantity == 3


def test_Item_init_default_quantity():
    item = Item('stuff', 12.34)
    assert item.name == 'stuff'
    assert item.unit_price == 12.34
    assert item.quantity == 1


@pytest.mark.parametrize(
    'unit_price, quantity, expected',
    [
        (12.34, 1, 12.34),
        (12.34, 3, 37.02),
        (12.34, 0, 0),
        (0, 1, 0),
    ]
)
def test_Item_calculate_item_total(unit_price, quantity, expected):
    item = Item('stuff', unit_price, quantity)
    assert expected == item.calculate_item_total()
