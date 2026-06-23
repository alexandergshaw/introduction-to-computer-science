"""
Assignment 2 — Variables and Deployment
=======================================
Week 2: variables, data types, and arithmetic.

Exercise: rectangle_area(width, height) returns the area of a rectangle.
  rectangle_area(3, 4) -> 12

Things to know:
  • A "parameter" (like width) is a named value handed to the function.
  • Python does math with the usual symbols:  +  -  *  /   (* means multiply).

Hint (no spoilers): the area of a rectangle is one side TIMES the other side.
"""


def rectangle_area(width: float, height: float) -> float:
    """Return width * height."""
    # "*" multiplies the two numbers; "return" hands the result back.
    return width * height
