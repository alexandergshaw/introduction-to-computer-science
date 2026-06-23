"""
Assignment 00 — Orientation
===========================
Your first file! Three tiny warm-up problems. Each is just a line of code,
and the full solutions are written in for you to read and run.

Problems:
  1. hello()             -> returns the string "Hello, world!"
  2. favorite_language() -> returns the name of the language we use
  3. double_text(text)   -> returns the text repeated twice ("ab" -> "abab")

Things to know:
  • A function hands back a value with the  return  keyword.
  • Text in quotes is a "string"; you can join strings together with  + .

Hint (no spoilers): for double_text, adding a string to itself repeats it.
"""


def hello() -> str:
    """Return the classic greeting."""
    return "Hello, world!"


def favorite_language() -> str:
    """Return the language this course uses."""
    return "Python"


def double_text(text: str) -> str:
    """Return text repeated twice."""
    # "ab" + "ab" -> "abab"
    return text + text
