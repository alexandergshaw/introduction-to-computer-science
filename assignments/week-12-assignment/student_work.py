"""
Assignment 12 — Advanced Unit Testing
=====================================
Week 12: functions worth testing across many inputs (think parametrized tests).
Pay attention to the edge cases described below.

Write each function so it matches the description, then run test_assignment.py
until all the tests pass.

What to build:
  1. clamp(n, low, high)    -> n if it is already within [low, high]; otherwise
                              the nearest boundary (low if too small, high if too big)
  2. in_range(n, low, high) -> True if n is between low and high, inclusive
  3. sign(n)                -> -1 if n is negative, 0 if it is zero, 1 if positive

Concepts you'll use:
  • min(x, y) returns the smaller of two values; max(x, y) returns the larger.
  • Python allows chained comparisons, e.g.  low <= n <= high .

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def clamp(n: float, low: float, high: float) -> float:
    """
    Return n limited to the inclusive range [low, high]: n itself if it's already
    inside the range, otherwise the nearest boundary.

    Example:
        clamp(5, 0, 10)  -> 5
        clamp(15, 0, 10) -> 10
        clamp(-4, 0, 10) -> 0
    """
    return max(low, min(n, high))


def in_range(n: float, low: float, high: float) -> bool:
    """
    Return True if n is between low and high (inclusive), otherwise False.

    Example:
        in_range(5, 0, 10)  -> True
        in_range(15, 0, 10) -> False
    """
    return low <= n <= high


def sign(n: float) -> int:
    """
    Return 1 if n is positive, -1 if n is negative, and 0 if n is zero.

    Example:
        sign(-3) -> -1
        sign(0)  -> 0
        sign(8)  -> 1
    """
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0
