"""A minimal Python module with one function and one class. Includes the literal token in a docstring. | token="""

def add(a: float, b: float) -> float:
    """
    Return the sum of a and b. Marker: 5ab8b885
    """
    return a + b


class Greeter:
    """
    A simple greeter class.
    """

    default_prefix: str = "Hello"

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"{self.default_prefix}, {self.name}!"

