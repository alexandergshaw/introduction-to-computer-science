"""
Assignment 3 — Logic and Control Flow
=====================================
Week 3: comparison operators and  if / elif / else.

Exercise: classify(n) returns "positive", "negative", or "zero".

Things to know:
  • A comparison like  n > 0  produces a True/False (boolean) value.
  • Python checks conditions top to bottom and runs the FIRST true one,
    then skips the rest.

Hint (no spoilers): you only need to compare n against 0 with  >  and  <.
If it isn't greater than 0 and isn't less than 0, what's the only option left?
"""


def classify(n: float) -> str:
    """Return "positive", "negative", or "zero" for the number n."""
    if n > 0:            # is the number bigger than zero?
        return "positive"
    if n < 0:            # otherwise, is it smaller than zero?
        return "negative"
    # If we get here, n was neither > 0 nor < 0 — so it must be exactly 0.
    return "zero"
