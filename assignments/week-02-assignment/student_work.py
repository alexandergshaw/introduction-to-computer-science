"""
Assignment 02 — Variables and Deployment
=========================================
Week 2: variables and arithmetic. Three short calculations.

Write each function so it returns the described value, then run
test_assignment.py until all the tests pass.

What to build:
  1. rectangle_area(width, height) -> the area of that rectangle
  2. square(n)                     -> n squared (n multiplied by itself)
  3. average(a, b)                 -> the average (mean) of the two numbers

Concepts you'll use:
  • Python's math operators:  +  -  *  /   (  *  multiplies,  /  divides).
  • Parentheses control the order of operations, just like in normal maths —
    what's inside the parentheses happens first.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def rectangle_area(width: float, height: float) -> float:
    """
    Return the area of a rectangle with the given width and height.

    Example:
        rectangle_area(3, 4) -> 12
    """
    return width * height


def square(n: float) -> float:
    """
    Return n squared (the result of multiplying n by itself).

    Example:
        square(4) -> 16
    """
    return n * n


def average(a: float, b: float) -> float:
    """
    Return the average (mean) of the two numbers a and b.

    Example:
        average(4, 6) -> 5
    """
    return (a + b) / 2
