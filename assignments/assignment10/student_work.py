"""
Assignment 10 — Error Handling and File I/O
===========================================
Week 10: try / except — reacting to errors instead of crashing.

Problems:
  1. safe_divide(a, b)        -> a / b, or None if b is 0
  2. to_int(text, default=0)  -> int(text), or default if text isn't a number
  3. safe_get(items, index)   -> items[index], or None if the index is out of range

Things to know:
  • "try" runs risky code; "except SomeError" catches that specific failure.
  • Dividing by 0 raises ZeroDivisionError; int("abc") raises ValueError;
    a bad list index raises IndexError.

Hint (no spoilers): attempt the normal action in try; in except, return the
safe fallback (None or default).
"""


def safe_divide(a: float, b: float):
    """Return a / b, or None if b is 0."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def to_int(text: str, default: int = 0) -> int:
    """Return text converted to an int, or default if that fails."""
    try:
        return int(text)
    except ValueError:
        return default


def safe_get(items: list, index: int):
    """Return items[index], or None if index is out of range."""
    try:
        return items[index]
    except IndexError:
        return None
