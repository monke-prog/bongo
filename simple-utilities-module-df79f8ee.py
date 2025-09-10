"""A tiny Python module with a simple function and a simple class. | token="""

def add(a, b):
    """Return the sum of a and b. Token: df79f8ee"""
    return a + b


class Counter:
    """A simple counter that can be incremented."""
    def __init__(self, start=0):
        self.value = start
    def increment(self, step=1):
        """Increase the counter by step and return the new value."""
        self.value += step
        return self.value

