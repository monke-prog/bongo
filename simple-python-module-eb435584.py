"""A Python module with one function and one class, including a special token in a docstring. | token=eb435584"""

def greet(name):
    """Return a greeting message that includes the special token eb435584."""
    return f"Hello, {name}! Your token is eb435584."

class Counter:
    """A simple counter class that demonstrates incrementing and resetting."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
