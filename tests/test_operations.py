# tests/test_operations.py
from decimal import Decimal
from typing import Callable  # Import Callable
from calculator.calculation import Calculation

def test_calculation_perform_addition():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x + y)
    assert calculation.perform() == Decimal('15')

def test_calculation_perform_subtraction():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x - y)
    assert calculation.perform() == Decimal('5')

def test_calculation_perform_multiplication():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x * y)
    assert calculation.perform() == Decimal('50')

def test_calculation_perform_division():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x / y)
    assert calculation.perform() == Decimal('2')

def test_calculation_repr_addition():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x + y)
    assert repr(calculation) == "Calculation(a=10, b=5, operation=<lambda>)"

def test_calculation_repr_subtraction():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x - y)
    assert repr(calculation) == "Calculation(a=10, b=5, operation=<lambda>)"

def test_calculation_repr_multiplication():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x * y)
    assert repr(calculation) == "Calculation(a=10, b=5, operation=<lambda>)"

def test_calculation_repr_division():
    calculation = Calculation(Decimal('10'), Decimal('5'), lambda x, y: x / y)
    assert repr(calculation) == "Calculation(a=10, b=5, operation=<lambda>)"
