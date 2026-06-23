"""
Assignment 0 — Orientation
==========================
Your very first Python file! The exercise is tiny: a function that hands
back a friendly greeting.

What's going on here?
  • A "function" is a reusable, named block of code. You "call" (run) it
    by writing its name followed by parentheses, like  hello().
  • "return" is how a function hands a value back to whoever called it.
  • Text wrapped in quotes (like "hi") is called a "string".

Hint (no spoilers): the test expects the classic two-word phrase almost
every programmer prints first. It starts with a capital H and ends with "!".
"""


def hello() -> str:
    """Return a greeting string."""
    # "return" sends this text back to the code that called hello().
    # (The "-> str" up in the definition just notes we return a string.)
    return "Hello, world!"
