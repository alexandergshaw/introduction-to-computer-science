"""
Assignment 11 — Unit Testing
============================
Week 11: small, predictable functions that are easy to test, including their
edge cases. Build the three functions described below.

Write each function so it matches the description, then run test_assignment.py
until all the tests pass.

What to build:
  1. is_palindrome(s) -> True if s reads the same forwards and backwards,
                         ignoring capitalisation; otherwise False
  2. is_even(n)       -> True if the whole number n is even; otherwise False
  3. absolute(n)      -> the size of n with no negative sign (its distance from 0)

Concepts you'll use:
  • A string has a  .lower()  method (a lowercase copy), useful for ignoring
    capitalisation.
  • Slice notation can reverse a sequence — look up the  [::-1]  slice.
  • The  %  (modulo) operator gives the remainder left after a division.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def is_palindrome(s: str) -> bool:
    """
    Return True if s reads the same forwards and backwards, ignoring
    capitalisation; otherwise False.

    Example:
        is_palindrome("racecar") -> True
        is_palindrome("hello")   -> False
    """
    cleaned = s.lower()
    return cleaned == cleaned[::-1]


def is_even(n: int) -> bool:
    """
    Return True if the whole number n is even, otherwise False.

    Example:
        is_even(4) -> True
        is_even(7) -> False
    """
    return n % 2 == 0


def absolute(n: float) -> float:
    """
    Return the absolute value of n — its distance from 0, which is never
    negative.

    Example:
        absolute(-3) -> 3
        absolute(5)  -> 5
    """
    if n < 0:
        return -n
    return n
