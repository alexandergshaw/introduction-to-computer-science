"""
Assignment 05 — Data Structures
===============================
Week 5: lists and sets, plus handy built-in helpers. Three short problems.

Problems:
  1. unique_sorted(items) -> the unique values, sorted ascending
  2. total(nums)          -> the sum of all the numbers
  3. largest(nums)        -> the biggest number in the list

Things to know:
  • A set() throws away duplicates; sorted() returns a new ordered list.
  • sum() adds up a list; max() finds the biggest item.

Hint (no spoilers): each problem is a one-liner using a built-in function.
"""


def unique_sorted(items: list) -> list:
    """Return the unique items in ascending order."""
    # Remove duplicates with set(), then order them with sorted().
    return sorted(set(items))


def total(nums: list) -> float:
    """Return the sum of nums."""
    return sum(nums)


def largest(nums: list) -> float:
    """Return the largest number in nums."""
    return max(nums)
