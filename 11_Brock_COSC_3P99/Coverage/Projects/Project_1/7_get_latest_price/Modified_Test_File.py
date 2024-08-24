import pytest
from core_functionality import DynamicallyPricedItem
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
    mocker.patch('integration_points.get_latest_price', return_value=unit_price)
    assert expected == item.calculate_item_total()


def test_DynamicallyPricedItem_get_latest_price(mocker):
    from integration_points import get_latest_price
    mock_response = Mock()
    mock_response.json.return_value = {'price': 12.34}
    mocker.patch('requests.get', return_value=mock_response)

    price = get_latest_price(12345)
    assert price == 12.34
