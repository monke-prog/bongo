"""A tiny Python module featuring a greet function and a Counter class. | token=d9eca072"""

def greet(name: str) -> str:
    """
    Return a friendly greeting. Token: d9eca072
    """
    return f"Hello, {name}!"

class Counter:
    """
    A simple counter class.
    """
    TOKEN = "d9eca072"

    def __init__(self, start: int = 0):
        self.value = start

    def increment(self, step: int = 1) -> int:
        """Increase the counter and return the new value."""
        self.value += step
        return self.value

    def __repr__(self) -> str:
        return f"Counter(value={self.value})"
