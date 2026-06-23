"""
Assignment 01 — Python Basics
=============================
Week 1: strings, simple functions, and f-strings. Three short problems.

Problems:
  1. greet(name)          -> "Hello, <name>!"      e.g. greet("Sam") -> "Hello, Sam!"
  2. loud(text)           -> the text in ALL CAPS  e.g. loud("hi")  -> "HI"
  3. add_excitement(text) -> the text with a "!" added at the end

Things to know:
  • An f-string (f"...") lets you drop a value into text with { }.
  • .upper() returns an all-uppercase copy of a string.

Hint (no spoilers): #1 slots name into the middle; #3 just joins on a "!".
"""


def greet(name: str) -> str:
    """Return a greeting that includes name."""
    return f"Hello, {name}!"


def loud(text: str) -> str:
    """Return text in uppercase."""
    return text.upper()


def add_excitement(text: str) -> str:
    """Return text with an exclamation point added."""
    return text + "!"
