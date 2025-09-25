"""A small Python module with one function and one class, including a specific token in a docstring. | token=e0e2c5a7"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token e0e2c5a7 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
