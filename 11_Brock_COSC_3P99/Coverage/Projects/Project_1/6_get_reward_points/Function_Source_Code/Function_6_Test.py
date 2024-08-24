# Function_6_Test.py

import pytest
from Function_6_Source import Order
from unittest.mock import Mock


def test_Order_get_reward_points(mocker):
    order = Order()
    subtotal_mock = mocker.patch.object(
        order, 'calculate_order_total', return_value=1000)
    assert order.get_reward_points() == 1010
