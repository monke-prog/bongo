"""A tiny Python module with one function and one class. Includes the literal token in a docstring. | token=d9aae8bf"""

def greet(name: str) -> str:
    """
    Return a friendly greeting for the provided name.

    Token for reference: d9aae8bf
    """
    return f"Hello, {name}!"

class Counter:
    """A simple integer counter."""

    def __init__(self, start: int = 0):
        self.value = int(start)

    def increment(self, step: int = 1) -> int:
        """Increase the counter by step and return the new value."""
        self.value += int(step)
        return self.value

    def reset(self) -> None:
        """Reset the counter to zero."""
        self.value = 0
