"""A tiny module with a sum function and a Greeter class. The class docstring contains the token. | token=5ab8b885"""

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


class Greeter:
    """A simple greeter class. Contains the token 5ab8b885 in this docstring."""

    def __init__(self, greeting: str = "Hello") -> None:
        self.greeting = greeting

    def greet(self, name: str) -> str:
        """Return a greeting addressed to the given name."""
        return f"{self.greeting}, {name}!"

