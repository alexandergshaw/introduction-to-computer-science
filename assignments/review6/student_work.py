"""
Student Work — Review 6: Review Module 1
=========================================
Week 6 is a review week — a chance to solidify everything you've
learned in Weeks 1 through 5 before moving forward.

──────────────────────────────────────────────────────
TOPICS TO REVIEW
──────────────────────────────────────────────────────
Use this week to revisit and strengthen your understanding of:

  WEEK 0 — Setup & GitHub Workflow
    □ Fork, Codespaces, and deploying with Vercel
    □ Branching off main
    □ Commit & push via the Source Control panel
    □ Opening a pull request and merging into main

  WEEK 1 — Python Basics
    □ Running a Python file in Codespaces
    □ print() and showing output
    □ Comments (#) and basic syntax
    □ Reading error messages / tracebacks

  WEEK 2 — Variables and Deployment
    □ Python data types: int, float, str, bool, None
    □ Variable naming rules (snake_case)
    □ How Vercel auto-deploys on push

  WEEK 3 — Logic and Control Flow
    □ Comparison operators: ==, !=, >, <, >=, <=
    □ Logical operators: and, or, not
    □ if / elif / else statements
    □ while loops (and avoiding infinite loops!)
    □ for loops and range()
    □ break and continue

  WEEK 4 — Functions and Modular Programming
    □ Defining functions with def
    □ Parameters and arguments
    □ Return values
    □ Default parameter values
    □ Variable scope (local vs global)
    □ Why modular code is better

  WEEK 5 — Data Structures
    □ Lists: indexing, slicing, append, remove, len
    □ Dictionaries: key-value pairs, .get(), .items()
    □ Tuples: immutability, unpacking
    □ Sets: uniqueness, fast lookup

──────────────────────────────────────────────────────
HOW TO REVIEW EFFECTIVELY
──────────────────────────────────────────────────────
  1. Re-read your notes and INSTRUCTIONS.md files from each week.
  2. Try to write code from memory — don't look it up right away.
  3. When you get stuck, THEN look at your previous student_work.py
     files for reference.
  4. Practice explaining concepts out loud as if teaching someone else.
     If you can explain it simply, you understand it!
  5. Identify your weakest topic and spend extra time there.

QUICK SELF-TEST — Can you answer these without help?
  • What is the difference between = and ==?
  • What does a function "return"?
  • What happens if you access list index 5 on a list with 3 items?
  • What is the difference between a list and a tuple?
  • What does the "not" operator do?

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for any specific review exercises.
2. Complete those exercises.
3. When finished, change MODULE_COMPLETED to True.

Review weeks are just as important as learning-new-content weeks.
Taking time to consolidate your knowledge now makes everything
in the second half of the semester much easier. 📚
"""

# ─── Exercise solution ──────────────────────────────────────────────────────
# Exercise: even_numbers(nums) returns just the even values, in their order.
#   even_numbers([1, 2, 3, 4]) -> [2, 4]
# Things to know:
#   • n % 2 is the REMAINDER when dividing n by 2. Even numbers leave 0.
#   • [ value for item in list if test ] is a "list comprehension": it builds
#     a new list, keeping only the items that pass the test.
# Hint (no spoilers): keep each number whose remainder after % 2 is 0.
def even_numbers(nums: list) -> list:
    """Return the even numbers from nums, preserving order."""
    # For every n in nums, keep it only when n % 2 == 0 (i.e. it's even).
    return [n for n in nums if n % 2 == 0]
