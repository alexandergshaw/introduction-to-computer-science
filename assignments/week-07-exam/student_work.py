"""
Exam 07 — Exam 1
================
Practice exam covering Weeks 0–6 (data types, control flow, functions, and data
structures). Three short problems at the same level as the weekly work.

Write each function so it matches the description, then run test_assignment.py
until all the tests pass.

What to build:
  1. letter_grade(score)   -> the letter grade for a 0–100 score, using the
                              standard cutoffs: 90+ = A, 80+ = B, 70+ = C,
                              60+ = D, below 60 = F
  2. average(nums)         -> the average (mean) of the numbers in the list
  3. count_positives(nums) -> how many numbers in the list are greater than 0

Concepts you'll use:
  • if / elif checks run top to bottom and the first true one wins, so the order
    of your cutoffs matters.
  • len(list) is how many items a list holds; sum(list) adds up its numbers.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def letter_grade(score: float) -> str:
    """
    Return the letter grade for a numeric score (0–100) using the standard
    cutoffs: 90+ = A, 80+ = B, 70+ = C, 60+ = D, anything below 60 = F.

    Example:
        letter_grade(95) -> "A"
        letter_grade(72) -> "C"
        letter_grade(40) -> "F"
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def average(nums: list) -> float:
    """
    Return the average (mean) of the numbers in nums.

    Example:
        average([2, 4, 6]) -> 4
    """
    return sum(nums) / len(nums)


def count_positives(nums: list) -> int:
    """
    Return how many numbers in nums are greater than 0.

    Example:
        count_positives([-1, 2, 0, 5]) -> 2
        count_positives([-3, -2])      -> 0
    """
    return len([n for n in nums if n > 0])
