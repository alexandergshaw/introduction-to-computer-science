"""
Assignment 01 — Python Basics
=============================
Week 1: strings, simple functions, and f-strings. Three short problems.

Write each function so its behaviour matches the description, then run
test_assignment.py until all the tests pass.

What to build:
  1. greet(name)          -> a greeting addressed to name, e.g.  Hello, Sam!
  2. loud(text)           -> the same text, but in ALL CAPS
  3. add_excitement(text) -> the same text with one exclamation point on the end

Concepts you'll use:
  • An f-string (written  f"..."  ) lets you drop a value into the middle of
    some text using  { } .
  • Strings have an  .upper()  method that returns an all-uppercase copy.
  • The  +  operator joins two strings together.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def greet(name: str) -> str:
    """
    Return a greeting addressed to name.

    Example:
        greet("Sam") -> "Hello, Sam!"
    """
    return f"Hello, {name}!"


def loud(text: str) -> str:
    """
    Return an all-uppercase version of text.

    Example:
        loud("hi") -> "HI"
    """
    return text.upper()


def add_excitement(text: str) -> str:
    """
    Return text with a single exclamation point added to the end.

    Example:
        add_excitement("go") -> "go!"
    """
    return text + "!"
