"""
Review 06 — Review 1
====================
A mixed review of Weeks 0–5: control flow, data structures, and functions.
Three short problems, one from each area.

Problems:
  1. classify(n)  -> "positive" / "negative" / "zero"   (control flow)
  2. total(nums)  -> the sum of a list of numbers        (data structures)
  3. greet(name)  -> "Hello, <name>!"                    (functions + strings)

Hint (no spoilers): these are the same kinds of one-liners you wrote in
Weeks 3, 5, and 1 — revisit those files if you get stuck.
"""


def classify(n: float) -> str:
    """Return "positive", "negative", or "zero" for n."""
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"


def total(nums: list) -> float:
    """Return the sum of nums."""
    return sum(nums)


def greet(name: str) -> str:
    """Return a greeting that includes name."""
    return f"Hello, {name}!"
