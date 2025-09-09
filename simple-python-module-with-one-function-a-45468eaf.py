"""A tiny module with one function and one class. | token="""

def greet(name: str) -> str:
    """Return a friendly greeting. Marker: 45468eaf"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter with increment and reset methods."""

    def __init__(self, start: int = 0) -> None:
        self._value = int(start)

    def increment(self, step: int = 1) -> int:
        self._value += int(step)
        return self._value

    def reset(self) -> None:
        self._value = 0

    @property
    def value(self) -> int:
        return self._value
