# combined_test_cases.py

import pytest
from Core_Functionality import Item

# --------------------------------------------------------------------------------
# Tests for Item initialization
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

# --------------------------------------------------------------------------------
# Tests for calculate_item_total method with boundary conditions and edge cases
# --------------------------------------------------------------------------------

@pytest.mark.parametrize(
    'unit_price, quantity, expected',
    [
        (12.34, 1, 12.34),  # Regular case
        (12.34, 3, 37.02),  # Multiple quantity
        (12.34, 0, 0),      # Quantity = 0
        (0, 1, 0),          # Unit price = 0
    ]
)
def test_Item_calculate_item_total(unit_price, quantity, expected):
    item = Item('stuff', unit_price, quantity)
    assert expected == item.calculate_item_total()

# --------------------------------------------------------------------------------
# Tests for Output Consistency
# --------------------------------------------------------------------------------

def test_Item_calculate_item_total_output_consistency():
    item = Item('stuff', 12.345, 1)
    assert item.calculate_item_total() == 12.35  # Rounded to two decimal places
