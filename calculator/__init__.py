# calculator/__init__.py
from calculator.calculations import Calculations
from decimal import Decimal
from typing import Callable  # Import Callable
from calculator.calculation import Calculation

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation(a, b, operation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, lambda x, y: x + y)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, lambda x, y: x - y)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, lambda x, y: x * y)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        if b == Decimal('0'):
            raise ValueError("Cannot divide by zero.")
        return Calculator._perform_operation(a, b, lambda x, y: x / y)