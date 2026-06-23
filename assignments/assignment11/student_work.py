"""
Assignment 11 — Unit Testing
============================
Week 11: writing assert-based tests and thinking about edge cases.

Exercise: is_palindrome(s) returns True if s reads the same backwards
(ignoring case).
  is_palindrome("racecar") -> True ; is_palindrome("hello") -> False
"""


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (case-insensitive)."""
    cleaned = s.lower()
    return cleaned == cleaned[::-1]
