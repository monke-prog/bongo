"""A minimal Python module exposing add() and Greeter, including the literal token in a docstring/string. | token="""

def add(a, b):
    """Return the sum of a and b. Token: 45468eaf"""
    return a + b


class Greeter:
    """A simple greeter class."""

    SECRET = "45468eaf"

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Return a greeting message."""
        return f"Hello, {self.name}!"

