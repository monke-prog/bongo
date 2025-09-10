"""A tiny module with a sum function and a greeter class. Includes the token in a docstring. | token="""

def add(a, b):
    """Return the sum of a and b. Token: df79f8ee"""
    return a + b


class Greeter:
    """Simple greeter class."""
    def __init__(self, name):
        self.name = name

    def greet(self):
        """Return a greeting message."""
        return f"Hello, {self.name}!"

