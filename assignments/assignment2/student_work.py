"""
Student Work — Assignment 2: Variables and Deployment
======================================================
Welcome to Week 2! This module is all about two foundational topics:

  1. VARIABLES — how Python stores and names data
  2. DEPLOYMENT — how to make your project live on the internet

──────────────────────────────────────────────────────
PART 1: PYTHON VARIABLES — A QUICK PRIMER
──────────────────────────────────────────────────────
A variable is a named storage location in memory.

    variable_name = value

You pick the name, Python remembers the value. Here are the most
common data types you'll use in Python:

  INTEGER (int)       — whole numbers, no decimal point
      age = 20
      score = 100
      year = 2025

  FLOAT (float)       — numbers with a decimal point
      gpa = 3.85
      price = 9.99
      temperature = 98.6

  STRING (str)        — text, wrapped in quotes
      name = "Maria Lopez"
      greeting = 'Hello, World!'
      course = "Introduction to CS"

  BOOLEAN (bool)      — True or False (no quotes!)
      is_enrolled = True
      has_submitted = False

  NONE (NoneType)     — the absence of a value
      result = None   # nothing assigned yet

VARIABLE NAMING RULES
----------------------
  ✓ Use lowercase letters and underscores: student_name, total_score
  ✓ Names must start with a letter or underscore, not a number
  ✗ Do NOT use spaces or hyphens: student name, student-name (broken!)
  ✗ Do NOT use Python reserved words as names: if, for, while, True, etc.

Python convention (called PEP 8) says to use "snake_case" for variables:
all lowercase letters with underscores between words.

REASSIGNING VARIABLES
----------------------
Variables can be changed at any time:

    score = 0        # score is 0
    score = score + 10   # now score is 10
    score += 5       # shorthand; now score is 15

──────────────────────────────────────────────────────
PART 2: DEPLOYMENT
──────────────────────────────────────────────────────
Deployment means publishing your project so other people can view it
on the internet. In Assignment 0 you deployed this dashboard to Vercel.

Every time you push code to GitHub, Vercel automatically re-deploys
the project. This is called "continuous deployment" (CD) — a core
concept in modern software development.

YOUR TASK
----------
1. Read INSTRUCTIONS.md for the full task details.
2. Practice working with variables as described in the instructions.
3. When you've completed all the steps, change MODULE_COMPLETED to True.

──────────────────────────────────────────────────────
HOW THE TEST CHECKS YOUR WORK
──────────────────────────────────────────────────────
The test simply checks that MODULE_COMPLETED is True and that
module_status() returns the same value.

TROUBLESHOOTING
---------------
  ✗ "assert module.MODULE_COMPLETED is True"
      → Change False to True (no quotes, capital T).

  ✗ SyntaxError on this file
      → Check that you didn't accidentally delete a line or add an
        invalid character while editing. Undo and try again.

Keep it up — you're building real skills! 🔥
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all module tasks.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function. It returns MODULE_COMPLETED for the test runner.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
