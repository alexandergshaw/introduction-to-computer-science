"""
Assignment 5 — Data Structures
==============================
Week 5: lists, sets, dictionaries, and tuples.

Exercise: unique_sorted(items) returns the unique values in ascending order.
  unique_sorted([3, 1, 3, 2]) -> [1, 2, 3]

Things to know:
  • A "set" automatically throws away duplicate values.
  • sorted(...) returns a NEW list arranged from smallest to largest.

Hint (no spoilers): two steps — first remove the duplicates, then put what's
left in order. Python has one built-in tool for each step.
"""


def unique_sorted(items: list) -> list:
    """Return the unique items in ascending order."""
    # set(items) drops duplicates; sorted(...) then orders them low -> high.
    return sorted(set(items))
