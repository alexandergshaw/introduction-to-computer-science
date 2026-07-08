"""
Assignment 10 — Error Handling and File I/O
===========================================
Week 10: using try / except so your code reacts to errors instead of crashing.
Each function attempts a normal action and returns a safe fallback if it fails.

Write each function so it returns the right value in BOTH the success case and
the failure case, then run test_assignment.py until all the tests pass.

What to build:
  1. safe_divide(a, b)       -> a divided by b, or None when b is 0
  2. to_int(text, default=0) -> text converted to a whole number, or default
                                when text isn't a valid number
  3. safe_get(items, index)  -> the item at that position in the list, or None
                                when the index is out of range

Concepts you'll use:
  • Code that might fail goes in a  try:  block; an  except SomeError:  block
    runs only when that specific error happens.
  • Dividing by 0 raises ZeroDivisionError, int("abc") raises ValueError, and an
    out-of-range list index raises IndexError.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def safe_divide(a: float, b: float):
    """
    Return a divided by b. If b is 0, return None instead of crashing.

    Example:
        safe_divide(6, 2) -> 3
        safe_divide(1, 0) -> None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def to_int(text: str, default: int = 0) -> int:
    """
    Return text converted to an integer. If text isn't a valid whole number,
    return default instead.

    Example:
        to_int("42")       -> 42
        to_int("abc")      -> 0
        to_int("abc", -1)  -> -1
    """
    try:
        return int(text)
    except ValueError:
        return default


def safe_get(items: list, index: int):
    """
    Return the item at position index in items. If index is out of range,
    return None.

    Example:
        safe_get([10, 20, 30], 1) -> 20
        safe_get([10, 20, 30], 9) -> None
    """
    try:
        return items[index]
    except IndexError:
        return None
