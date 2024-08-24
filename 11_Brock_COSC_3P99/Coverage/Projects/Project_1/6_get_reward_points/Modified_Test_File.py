# combined_test.py

import pytest
from unittest.mock import Mock, patch
from Core_Functionality import Order
from boundary_conditions import BoundaryConditions
from integration_points import IntegrationPoints
from output_consistency import OutputConsistency

# --------------------------------------------------------------------------------
# Core Functionality Tests
# --------------------------------------------------------------------------------

def test_Order_get_reward_points(mocker):
    order = Order()
    subtotal_mock = mocker.patch.object(
        order, 'calculate_order_total', return_value=1000)
    assert order.get_reward_points() == 1010

# --------------------------------------------------------------------------------
# Boundary Conditions and Edge Cases Tests
# --------------------------------------------------------------------------------

def test_calculate_total_negatives():
    order = BoundaryConditions()

    with pytest.raises(ValueError):
        order.calculate_total(-100, 10, 5, 0.05)
    with pytest.raises(ValueError):
        order.calculate_total(100, -10, 5, 0.05)
    with pytest.raises(ValueError):
        order.calculate_total(100, 10, -5, 0.05)
    with pytest.raises(ValueError):
        order.calculate_total(100, 10, 5, -0.05)

# --------------------------------------------------------------------------------
# Integration Points Tests
# --------------------------------------------------------------------------------

def test_calculate_order_total():
    order = IntegrationPoints()
    order.add_item(Mock(calculate_item_total=lambda: 100))
    order.add_item(Mock(calculate_item_total=lambda: 200))
    assert order.calculate_order_total() == 315.0  # Assuming specific tax, shipping, etc.

# --------------------------------------------------------------------------------
# Output Consistency Tests
# --------------------------------------------------------------------------------

def test_calculate_total_output_consistency():
    order = OutputConsistency()
    result = order.calculate_total(100, 20, 10, 0.05)
    assert result == 115.50
