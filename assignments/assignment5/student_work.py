"""
Assignment 5 — Data Structures
==============================
Week 5: lists, sets, dictionaries, and tuples.

Exercise: unique_sorted(items) returns the unique values, sorted ascending.
  unique_sorted([3, 1, 3, 2]) -> [1, 2, 3]
"""


def unique_sorted(items: list) -> list:
    """Return the unique items in ascending order."""
    return sorted(set(items))
