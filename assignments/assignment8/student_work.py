"""
Assignment 8 — OOP: Classes
===========================
Week 8: classes, __init__, self, instance attributes and methods.

Exercise: Rectangle(width, height) with an area() method.
  Rectangle(2, 3).area() -> 6
"""


class Rectangle:
    """A simple rectangle."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return width * height."""
        return self.width * self.height
