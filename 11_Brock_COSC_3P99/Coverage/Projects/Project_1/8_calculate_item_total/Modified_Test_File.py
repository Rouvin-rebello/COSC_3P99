import pytest
from Function_8_Core import Item, DynamicallyPricedItem
from Function_8_Boundary import Item as BoundaryItem
from Function_8_ErrorHandling import Item as ErrorHandlingItem
from Function_8_Integration import DynamicallyPricedItem as IntegrationItem
from unittest.mock import Mock

# --------------------------------------------------------------------------------
# Tests for Core Functionality
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


# --------------------------------------------------------------------------------
# Tests for Boundary Conditions and Edge Cases
# --------------------------------------------------------------------------------

def test_BoundaryItem_init_negative_quantity():
    with pytest.raises(ValueError) as e:
        BoundaryItem('stuff', 12.34, -1)
    assert str(e.value) == 'Quantity cannot be negative'


# --------------------------------------------------------------------------------
# Tests for Error Handling
# --------------------------------------------------------------------------------

def test_ErrorHandlingItem_calculate_item_total_negative_total():
    item = ErrorHandlingItem('stuff', -12.34, 3)
    with pytest.raises(ValueError) as e:
        item.calculate_item_total()
    assert str(e.value) == 'Total cannot be negative'


# --------------------------------------------------------------------------------
# Tests for Integration Points
# --------------------------------------------------------------------------------

@pytest.mark.parametrize(
    'unit_price, quantity, expected',
    [
        (12.34, 1, 12.34),
        (12.34, 3, 37.02),
        (12.34, 0, 0),
        (0, 1, 0),
    ]
)
def test_IntegrationItem_calculate_item_total(mocker, unit_price, quantity, expected):
    item = IntegrationItem(12345, quantity)
    mocker.patch.object(item, 'get_latest_price', return_value=unit_price)
    assert expected == item.calculate_item_total()


def test_IntegrationItem_get_latest_price(mocker):
    item = IntegrationItem(12345)
    mock_response = Mock()
    mock_response.json.return_value = {'price': 12.34}
    mocker.patch('requests.get', return_value=mock_response)

    price = item.get_latest_price()
    assert price == 12.34
