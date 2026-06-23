"""
Assignment 3 — Logic and Control Flow
=====================================
Week 3: comparison operators and if / elif / else.

Exercise: classify(n) returns "positive", "negative", or "zero".
"""


def classify(n: float) -> str:
    """Classify a number as positive, negative, or zero."""
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"
