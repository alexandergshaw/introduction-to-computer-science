"""
Review 06 — Review 1
====================
A mixed review of Weeks 0–5: control flow, data structures, and functions — one
short problem from each area. You've written this kind of function before; if you
get stuck, revisit the earlier week noted in parentheses.

Write each function so it matches the description, then run test_assignment.py
until all the tests pass.

What to build:
  1. classify(n) -> "positive", "negative", or "zero" depending on n   (Week 3)
  2. total(nums) -> the sum of all the numbers in the list nums         (Week 5)
  3. greet(name) -> a greeting of the form  Hello, <name>!              (Week 1)

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def classify(n: float) -> str:
    """
    Return "positive" if n is greater than 0, "negative" if it is less than 0,
    and "zero" if it is exactly 0.

    Example:
        classify(5)  -> "positive"
        classify(0)  -> "zero"
    """
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"


def total(nums: list) -> float:
    """
    Return the sum of all the numbers in nums.

    Example:
        total([1, 2, 3]) -> 6
    """
    return sum(nums)


def greet(name: str) -> str:
    """
    Return a greeting of the form "Hello, <name>!".

    Example:
        greet("Sam") -> "Hello, Sam!"
    """
    return f"Hello, {name}!"
