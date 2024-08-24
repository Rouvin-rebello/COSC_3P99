import pytest
from core_functionality import core_calculate_total
from boundary_conditions import boundary_calculate_total
from error_handling import error_handling_calculate_total

# --------------------------------------------------------------------------------
# Tests for calculate_total - Core Functionality
# --------------------------------------------------------------------------------

@pytest.mark.parametrize(
    'subtotal, shipping, discount, tax_percent, expected',
    [
        (90, 10, 20, 0.05, 84.00),
        (0, 10, 5, 0.05, 5.25),
        (90, 0, 20, 0.05, 73.50),
        (90, 10, 0, 0.05, 105.00),
        (90, 10, 20, 0, 80.00),
        (10, 5, 5, 0.0875, 10.88),
        (10, 5, 5, 0.0733, 10.73),
        (10, 10, 20, 0.05, 0.00),
        (10, 5, 20, 0.05, 0.00),
    ]
)
def test_core_calculate_total(subtotal, shipping, discount, tax_percent, expected):
    assert core_calculate_total(subtotal, shipping, discount, tax_percent) == expected


# --------------------------------------------------------------------------------
# Tests for calculate_total - Boundary Conditions and Edge Cases
# --------------------------------------------------------------------------------

@pytest.mark.parametrize(
    'subtotal, shipping, discount, tax_percent, expected',
    [
        (90, 10, 20, 0.05, 84.00),
        (0, 10, 5, 0.05, 5.25),
        (90, 0, 20, 0.05, 73.50),
        (90, 10, 0, 0.05, 105.00),
        (90, 10, 20, 0, 80.00),
        (10, 5, 5, 0.0875, 10.88),
        (10, 5, 5, 0.0733, 10.73),
        (10, 10, 20, 0.05, 0.00),
        (10, 5, 20, 0.05, 0.00),
    ]
)
def test_boundary_calculate_total(subtotal, shipping, discount, tax_percent, expected):
    assert boundary_calculate_total(subtotal, shipping, discount, tax_percent) == expected


# --------------------------------------------------------------------------------
# Tests for calculate_total - Error Handling
# --------------------------------------------------------------------------------

@pytest.mark.parametrize(
    'subtotal, shipping, discount, tax_percent, variable',
    [
        (-90, 10, 20, 0.05, 'subtotal'),
        (90, -10, 20, 0.05, 'shipping'),
        (90, 10, -20, 0.05, 'discount'),
        (90, 10, 20, -0.05, 'tax_percent'),
    ]
)
def test_error_handling_calculate_total(subtotal, shipping, discount, tax_percent, variable):
    with pytest.raises(ValueError) as e:
        error_handling_calculate_total(subtotal, shipping, discount, tax_percent)
    assert str(e.value) == f'{variable} cannot be negative'
