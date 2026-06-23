"""
Assignment 11 — Unit Testing
============================
Week 11: small, easy-to-test functions (and edge cases). Three problems.

Problems:
  1. is_palindrome(s) -> True if s reads the same backwards (ignoring case)
  2. is_even(n)       -> True if n is even
  3. absolute(n)      -> the distance from 0 (always 0 or positive)

Things to know:
  • s.lower() ignores capitalization; s[::-1] is the string reversed.
  • n % 2 == 0 tests for even.

Hint (no spoilers): a palindrome equals its own reverse; absolute flips the
sign only when n is negative.
"""


def is_palindrome(s: str) -> bool:
    """Return True if s is the same backwards (case-insensitive)."""
    cleaned = s.lower()
    return cleaned == cleaned[::-1]


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def absolute(n: float) -> float:
    """Return the absolute value of n (its distance from 0)."""
    if n < 0:
        return -n
    return n
