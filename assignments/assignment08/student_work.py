"""
Assignment 08 — OOP: Classes
============================
Week 8: writing your own classes with __init__, self, and methods. Build three
small classes so their objects behave as described below.

Write the code so each object behaves correctly, then run test_assignment.py
until all the tests pass.

What to build:
  1. Rectangle(width, height) — remembers its width and height.
       .area()  returns the rectangle's area.
  2. Square(side)             — remembers its side length.
       .area()  returns the square's area.
  3. Person(name)             — remembers a name.
       .greet() returns a short self-introduction of the form  Hi, I'm <name>

Concepts you'll use:
  • __init__ runs automatically when an object is created, e.g. Rectangle(2, 3).
  • "self" refers to THIS particular object; you store values on it by writing
    something like  self.width = width .
  • A method can read the values saved on  self  to work out its answer.

Tip: open test_assignment.py to see exactly how each object is created and used.
"""


class Rectangle:
    """A rectangle built from a width and a height."""

    def __init__(self, width: float, height: float) -> None:
        """Remember this rectangle's width and height for later."""
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Return this rectangle's area.

        Example:
            Rectangle(3, 4).area() -> 12
        """
        return self.width * self.height


class Square:
    """A square built from one side length."""

    def __init__(self, side: float) -> None:
        """Remember this square's side length for later."""
        self.side = side

    def area(self) -> float:
        """
        Return this square's area.

        Example:
            Square(5).area() -> 25
        """
        return self.side * self.side


class Person:
    """A person with a name."""

    def __init__(self, name: str) -> None:
        """Remember this person's name for later."""
        self.name = name

    def greet(self) -> str:
        """
        Return a short self-introduction of the form "Hi, I'm <name>".

        Example:
            Person("Ada").greet() -> "Hi, I'm Ada"
        """
        return f"Hi, I'm {self.name}"
