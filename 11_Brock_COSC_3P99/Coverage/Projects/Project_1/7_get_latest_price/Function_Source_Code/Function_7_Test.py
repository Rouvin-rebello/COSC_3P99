import pytest
from Function_7_Source import DynamicallyPricedItem
from unittest.mock import Mock


@pytest.mark.parametrize(
    'unit_price, quantity, expected',
    [
        (12.34, 1, 12.34),
        (12.34, 3, 37.02),
        (12.34, 0, 0),
        (0, 1, 0),
    ]
)
def test_DynamicallyPricedItem_calculate_item_total(mocker, unit_price, quantity, expected):
    item = DynamicallyPricedItem(12345, quantity)
    mocker.patch.object(item, 'get_latest_price', return_value=unit_price)
    assert expected == item.calculate_item_total()


def test_DynamicallyPricedItem_get_latest_price(mocker):
    item = DynamicallyPricedItem(12345)
    mock_response = Mock()
    mock_response.json.return_value = {'price': 12.34}
    mocker.patch('requests.get', return_value=mock_response)

    price = item.get_latest_price()
    assert price == 12.34
