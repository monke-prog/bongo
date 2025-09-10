"""A small Python module with one simple function and one simple class. | token=d9aae8bf"""

def add(a: float, b: float) -> float:
    """Add two numbers and return the result. token: d9aae8bf"""
    return a + b


class Greeter:
    """A simple greeter class."""

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        """Return a friendly greeting."""
        return f"Hello, {self.name}!"

