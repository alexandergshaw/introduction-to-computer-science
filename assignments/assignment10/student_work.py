"""
Assignment 10 — Error Handling and File I/O
===========================================
Week 10: try / except, exception types, and reading/writing files with "with".

Exercise: safe_divide(a, b) returns a / b, or None if b is 0.
  safe_divide(6, 2) -> 3.0 ; safe_divide(1, 0) -> None
"""


def safe_divide(a: float, b: float):
    """Return a / b, or None if dividing by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None
