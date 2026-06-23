"""
Assignment 10 — Error Handling and File I/O
===========================================
Week 10: try / except, and handling errors gracefully.

Exercise: safe_divide(a, b) returns a / b, but if b is 0 it returns None
instead of crashing.
  safe_divide(6, 2) -> 3.0      safe_divide(1, 0) -> None

Things to know:
  • Dividing by zero normally CRASHES with a ZeroDivisionError.
  • "try / except" lets you attempt risky code and react if it fails.
  • None is Python's way of saying "no value".

Hint (no spoilers): try the division; if the zero-division error happens,
catch it and return None instead of letting the program crash.
"""


def safe_divide(a: float, b: float):
    """Return a / b, or None if b is 0."""
    try:
        # This line is the risky part: it blows up if b is 0.
        return a / b
    except ZeroDivisionError:
        # We only land here when the division failed because b was 0.
        return None
