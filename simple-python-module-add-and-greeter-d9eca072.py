"""A minimal module with one function and one class, including the token in a docstring. | token="""

def add(a: int, b: int) -> int:
    """Return the sum of a and b. Token: d9eca072"""
    return a + b


class Greeter:
    """A simple greeter class."""
    SECRET = "d9eca072"

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a friendly greeting for the configured name."""
        return f"Hello, {self.name}!"

