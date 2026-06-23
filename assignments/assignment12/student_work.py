"""
Assignment 12 — Advanced Unit Testing
=====================================
Week 12: functions worth testing with many inputs (think parametrized tests).

Problems:
  1. clamp(n, low, high)    -> keep n inside the range [low, high]
  2. in_range(n, low, high) -> True if low <= n <= high
  3. sign(n)                -> -1 if negative, 0 if zero, 1 if positive

Things to know:
  • min(x, y) gives the smaller value; max(x, y) gives the larger.
  • Python lets you chain comparisons:  low <= n <= high.

Hint (no spoilers): clamp pulls n down to high if it's too big and up to low
if it's too small — min() and max() together do both.
"""


def clamp(n: float, low: float, high: float) -> float:
    """Constrain n to the inclusive range [low, high]."""
    return max(low, min(n, high))


def in_range(n: float, low: float, high: float) -> bool:
    """Return True if n is between low and high (inclusive)."""
    return low <= n <= high


def sign(n: float) -> int:
    """Return -1, 0, or 1 depending on the sign of n."""
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0
