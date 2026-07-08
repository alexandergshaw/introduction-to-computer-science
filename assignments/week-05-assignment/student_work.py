"""
Assignment 05 — Data Structures
===============================
Week 5: lists and sets, plus some handy built-in helper functions.

Write each function so it returns the described value, then run
test_assignment.py until all the tests pass.

What to build:
  1. unique_sorted(items) -> the values from items with duplicates removed,
                             arranged in ascending order
  2. total(nums)          -> the sum of all the numbers in the list
  3. largest(nums)        -> the biggest number in the list

Concepts you'll use:
  • A  set()  drops duplicate values;  sorted()  returns a new list in order.
  • sum()  adds up the numbers in a list;  max()  finds the largest item.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def unique_sorted(items: list) -> list:
    """
    Return a list of the unique values from items, sorted in ascending order.

    Example:
        unique_sorted([3, 1, 2, 1]) -> [1, 2, 3]
    """
    return sorted(set(items))


def total(nums: list) -> float:
    """
    Return the sum of all the numbers in nums.

    Example:
        total([1, 2, 3]) -> 6
    """
    return sum(nums)


def largest(nums: list) -> float:
    """
    Return the largest number in nums.

    Example:
        largest([4, 9, 2]) -> 9
    """
    return max(nums)
