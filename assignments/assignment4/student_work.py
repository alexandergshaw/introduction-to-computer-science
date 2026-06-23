"""
Assignment 4 — Functions and Modular Programming
================================================
Week 4: defining functions, parameters, return values, and default values.

Exercise: add(a, b, c=0) returns the sum; the third argument is optional.
  add(2, 3) -> 5 ; add(2, 3, 4) -> 9
"""


def add(a: float, b: float, c: float = 0) -> float:
    """Return the sum of two or three numbers (the third defaults to 0)."""
    return a + b + c
