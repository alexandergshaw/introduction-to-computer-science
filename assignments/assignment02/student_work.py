"""
Assignment 02 — Variables and Deployment
=========================================
Week 2: variables and arithmetic. Three short calculations.

Problems:
  1. rectangle_area(width, height) -> width * height
  2. square(n)                     -> n multiplied by itself
  3. average(a, b)                 -> the mean of two numbers, (a + b) / 2

Things to know:
  • Python math symbols:  +  -  *  /   (* is multiply, / is divide).
  • Use parentheses to control the order:  (a + b) / 2  adds first, then divides.

Hint (no spoilers): a square's area is a side times itself.
"""


def rectangle_area(width: float, height: float) -> float:
    """Return width * height."""
    return width * height


def square(n: float) -> float:
    """Return n times itself."""
    return n * n


def average(a: float, b: float) -> float:
    """Return the average of a and b."""
    # Add the two numbers first, THEN divide by 2.
    return (a + b) / 2
