"""A small Python module with one function and one class. Includes the literal token in a docstring. | token=466f79ef"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


class Greeter:
    """A simple greeter.

    Token: 466f79ef
    """
    def __init__(self, name="World"):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

