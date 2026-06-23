"""
Assignment 1 — Python Basics
============================
Week 1: running Python, printing, comments, and simple functions.

Exercise: greet(name) builds a greeting that includes the given name.
  greet("Sam") -> "Hello, Sam!"

Things to know:
  • Anything after a  #  is a COMMENT — Python ignores it. It's a note for
    humans (exactly like this line!).
  • An f-string (a string with an  f  before the opening quote) lets you drop
    a value straight into the text using { }, e.g.  f"Hi {name}".

Hint (no spoilers): the name arrives as the "name" parameter. Slot it into
the middle of the greeting so "Sam" becomes "Hello, Sam!".
"""


def greet(name: str) -> str:
    """Return a greeting that includes name."""
    # The {name} below is replaced by whatever was passed in.
    # Picture greet("Ada"): name is "Ada", so this becomes "Hello, Ada!".
    return f"Hello, {name}!"
