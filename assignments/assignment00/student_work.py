"""
Assignment 00 — Orientation
===========================
Your very first file. Three tiny warm-up functions to get you used to the loop
of "edit the code, then run the tests." Each one is a single line of code.

How this works: every function below has a description (and usually an example)
telling you exactly what it should hand back. Write code so the behaviour
matches, then run test_assignment.py from the Testing panel until all the tests
turn green.

What to build:
  1. hello()             -> the exact text  Hello, world!
  2. favorite_language() -> the name of the programming language this course uses
  3. double_text(text)   -> the given text written out twice in a row

Concepts you'll use:
  • A function hands a value back to whoever called it with the  return  keyword.
  • Text wrapped in quotes is called a "string".
  • Two strings can be combined into one longer string with the  +  operator.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def hello() -> str:
    """Return the exact text: Hello, world!"""
    return "Hello, world!"


def favorite_language() -> str:
    """Return the name of the programming language this course is taught in."""
    return "Python"


def double_text(text: str) -> str:
    """
    Return text written out twice in a row, with nothing in between.

    Example:
        double_text("ab") -> "abab"
    """
    return text + text
