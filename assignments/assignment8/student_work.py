"""
Assignment 8 — OOP: Classes
===========================
Week 8: classes, __init__, self, and instance methods.

Exercise: a Rectangle class built from a width and height, with an area() method.
  Rectangle(2, 3).area() -> 6

Things to know:
  • A "class" is a blueprint for making objects.
  • __init__ runs automatically when you create one, e.g. Rectangle(2, 3).
  • "self" means "this particular object", so self.width is THIS rectangle's width.

Hint (no spoilers): save the two sides in __init__, then have area() multiply
this rectangle's own two sides together.
"""


class Rectangle:
    """A rectangle described by a width and a height."""

    def __init__(self, width: float, height: float) -> None:
        # Save the values ONTO this object so other methods can use them later.
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return this rectangle's area."""
        # self.width and self.height are the values saved in __init__.
        return self.width * self.height
