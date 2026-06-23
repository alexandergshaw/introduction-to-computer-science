"""
Exam 07 — Exam 1
================
Practice exam covering Weeks 0–6 (data types, control flow, functions,
data structures). Three short problems at the same easy level.

Problems:
  1. letter_grade(score)  -> "A"/"B"/"C"/"D"/"F" for a 0–100 score
  2. average(nums)        -> the mean of a list, sum(nums) / len(nums)
  3. count_positives(nums)-> how many numbers in the list are greater than 0

Things to know:
  • if / elif checks run top to bottom; the first true one wins.
  • len(nums) is how many items are in the list.

Hint (no spoilers): for the grade, check the highest cutoff first; for the
count, go through the list and tally the ones above 0.
"""


def letter_grade(score: float) -> str:
    """Return the letter grade for a numeric score (0–100)."""
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
    """Return the average (mean) of nums."""
    return sum(nums) / len(nums)


def count_positives(nums: list) -> int:
    """Return how many numbers in nums are greater than 0."""
    # Keep just the positives, then count them with len().
    return len([n for n in nums if n > 0])
