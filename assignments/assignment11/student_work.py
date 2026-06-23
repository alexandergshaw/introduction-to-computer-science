"""
Assignment 11 — Unit Testing
============================
Week 11: writing tests and thinking about edge cases.

Exercise: is_palindrome(s) is True if s reads the same forwards and backwards
(ignoring capital letters).
  is_palindrome("racecar") -> True      is_palindrome("hello") -> False

Things to know:
  • s.lower() makes the text all lowercase, so "Anna" still counts.
  • s[::-1] is a handy Python trick that gives you the string REVERSED.
  • Comparing two strings with  ==  gives back True or False.

Hint (no spoilers): make the text lowercase, then check whether it equals
its own reverse.
"""


def is_palindrome(s: str) -> bool:
    """Return True if s is the same backwards (case-insensitive)."""
    cleaned = s.lower()            # ignore capitalization first
    # cleaned[::-1] is "cleaned" spelled backwards; == checks if they match.
    return cleaned == cleaned[::-1]
