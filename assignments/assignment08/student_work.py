"""
Assignment 08 — OOP: Classes
============================
Week 8: classes, __init__, self, and methods. Three small classes.

Problems:
  1. Rectangle(width, height) with .area()  -> width * height
  2. Square(side)            with .area()    -> side * side
  3. Person(name)            with .greet()   -> "Hi, I'm <name>"

Things to know:
  • __init__ runs when you build the object, e.g. Rectangle(2, 3).
  • "self" means THIS object; self.width is this rectangle's own width.

Hint (no spoilers): save the values in __init__, then use them in the method.
"""


class Rectangle:
    """A rectangle built from a width and a height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return this rectangle's area."""
        return self.width * self.height


class Square:
    """A square built from one side length."""

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        """Return this square's area."""
        return self.side * self.side


class Person:
    """A person with a name."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a short self-introduction."""
        return f"Hi, I'm {self.name}"
