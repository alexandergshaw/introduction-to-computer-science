"""
Assignment 03 — Logic and Control Flow
======================================
Week 3: comparisons and if / elif / else. Three short decisions.

Write each function so it returns the described value, then run
test_assignment.py until all the tests pass.

What to build:
  1. classify(n)   -> "positive", "negative", or "zero" depending on n
  2. is_even(n)    -> True if n is even, otherwise False
  3. larger(a, b)  -> whichever of the two numbers is bigger

Concepts you'll use:
  • A comparison such as  n > 0  evaluates to True or False.
  • if / elif / else lets your code choose between different branches.
  • The  %  (modulo) operator gives the remainder left after a division.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def classify(n: float) -> str:
    """
    Return "positive" if n is greater than 0, "negative" if it is less than 0,
    and "zero" if it is exactly 0.

    Example:
        classify(5)  -> "positive"
        classify(0)  -> "zero"
    """
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"


def is_even(n: int) -> bool:
    """
    Return True if the whole number n is even, otherwise False.

    Example:
        is_even(4) -> True
        is_even(7) -> False
    """
    return n % 2 == 0


def larger(a: float, b: float) -> float:
    """
    Return whichever of a and b is larger.

    Example:
        larger(3, 9) -> 9
    """
    if a > b:
        return a
    return b
