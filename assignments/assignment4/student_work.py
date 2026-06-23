"""
Assignment 4 — Functions and Modular Programming
================================================
Week 4: parameters, return values, and DEFAULT parameter values.

Exercise: add(a, b, c=0) adds the numbers; the third one is optional.
  add(2, 3)    -> 5   (c defaults to 0, so 2 + 3 + 0)
  add(2, 3, 4) -> 9   (now c is 4, so 2 + 3 + 4)

Things to know:
  • Writing  c=0  gives c a DEFAULT value. If the caller leaves it out,
    c is automatically 0.

Hint (no spoilers): add all three parameters together and return the total.
Because c defaults to 0, leaving it off doesn't change the sum.
"""


def add(a: float, b: float, c: float = 0) -> float:
    """Return a + b + c (c is optional and defaults to 0)."""
    return a + b + c
