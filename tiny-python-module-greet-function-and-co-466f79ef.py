"""A minimal Python module with one simple function and one simple class. Includes the token in a docstring. | token=466f79ef"""

def greet(name: str) -> str:
    """Return a friendly greeting. Token: 466f79ef"""
    return f"Hello, {name}!"

class Counter:
    """A tiny counter class that increments an integer value."""
    def __init__(self, start: int = 0):
        self.value = int(start)

    def increment(self, step: int = 1) -> int:
        """Increase by step and return the new value."""
        self.value += int(step)
        return self.value
