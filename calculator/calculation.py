# calculator/calculation.py
from decimal import Decimal
from typing import Callable  # Import Callable

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)

    def __repr__(self) -> str:
        return f"Calculation(a={self.a}, b={self.b}, operation={self.operation.__name__})"
