from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        if not isinstance(a, Decimal) or not isinstance(b, Decimal):
            raise ValueError("Both a and b must be of type Decimal")
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(cls, a, b, operation):
        """Factory method to create a Calculation instance."""
        return cls(a, b, operation)

    def perform(self):
        """Perform the calculation based on the operation provided."""
        if self.operation is None:
            raise ValueError("Unknown operation")

        if self.operation == divide and self.b == Decimal('0'):
            raise ValueError("Cannot divide by zero")

        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a string representation of the Calculation object."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
