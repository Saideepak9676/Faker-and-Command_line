# tests/test_calculator.py
from decimal import Decimal
from calculator import Calculator

def test_addition():
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4')

def test_subtraction():
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0')

def test_multiply():
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4')

def test_divide():
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1')

def test_divide_by_zero():
    try:
        Calculator.divide(Decimal('2'), Decimal('0'))
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
