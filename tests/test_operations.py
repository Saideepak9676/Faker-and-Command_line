import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_operation(a, b, operation, expected):
    """Test various arithmetic operations."""
    calculation = Calculation.create(a, b, operation)
    result = calculation.perform()
    assert result == expected, f"{operation.__name__} operation failed"


def test_divide_by_zero():
    """Test division by zero exception handling."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
