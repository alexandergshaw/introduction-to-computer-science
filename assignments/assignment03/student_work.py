"""
Assignment 03 — Logic and Control Flow
======================================
Week 3: comparisons and if / elif / else. Three short decisions.

Problems:
  1. classify(n)   -> "positive", "negative", or "zero"
  2. is_even(n)    -> True if n is even, otherwise False
  3. larger(a, b)  -> the bigger of the two numbers

Things to know:
  • A comparison like  n > 0  gives back True or False.
  • n % 2 is the remainder after dividing by 2; even numbers leave 0.

Hint (no spoilers): for larger, compare the two and return whichever wins.
"""


def classify(n: float) -> str:
    """Return "positive", "negative", or "zero" for n."""
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"   # not > 0 and not < 0 means it must be 0


def is_even(n: int) -> bool:
    """Return True if n is even."""
    # An even number divides by 2 with no remainder.
    return n % 2 == 0


def larger(a: float, b: float) -> float:
    """Return the larger of a and b."""
    if a > b:
        return a
    return b
