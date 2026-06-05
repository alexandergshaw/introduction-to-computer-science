"""
Student Work — Assignment 13: Best Practices
=============================================
Week 13 is about writing code that's not just correct, but also
clean, readable, and maintainable. These are the habits that
separate good programmers from great ones.

──────────────────────────────────────────────────────
WHY BEST PRACTICES MATTER
──────────────────────────────────────────────────────
Most code is read far more often than it's written. You'll read your
own code days, weeks, or months later and wonder "what was I thinking?"
Other developers will read your code too.

Clean code:
  ✓ Is easier to understand (fewer bugs introduced by confusion)
  ✓ Is easier to debug and fix
  ✓ Is easier to extend and modify later
  ✓ Makes you a better collaborator

The single best question to ask yourself as you write code:
"Would a reasonable developer understand this in 30 seconds?"

──────────────────────────────────────────────────────
PEP 8 — PYTHON'S STYLE GUIDE
──────────────────────────────────────────────────────
PEP 8 is the official Python style guide. Most Python teams follow it.
Key rules:

  INDENTATION
    • Use 4 spaces per indentation level (not tabs)

  NAMING CONVENTIONS
    • Variables and functions: snake_case  → total_score, get_user_name
    • Classes:                 PascalCase → BankAccount, StudentRecord
    • Constants:               UPPER_CASE → MAX_SIZE, DEFAULT_TIMEOUT
    • "Private" members:       _single_leading_underscore

  LINE LENGTH
    • Maximum 79 characters per line (allows side-by-side file viewing)

  BLANK LINES
    • 2 blank lines before and after top-level functions/classes
    • 1 blank line between methods inside a class

  IMPORTS
    • One import per line (not: import os, sys)
    • Standard library first, then third-party, then your own modules

  WHITESPACE
    • Spaces around operators:  x = 5 + 3  (not: x=5+3)
    • No space before colon in slices: list[1:3]
    • Space after commas: func(a, b, c)

──────────────────────────────────────────────────────
DOCSTRINGS — DOCUMENTING YOUR CODE
──────────────────────────────────────────────────────
A docstring is a string literal that appears as the first statement
in a module, function, class, or method. It describes what it does.

  MODULE docstring (top of the file):
    '''This module provides utility functions for string processing.'''

  FUNCTION docstring:
    def calculate_area(radius: float) -> float:
        '''
        Calculate the area of a circle.

        Args:
            radius: The radius of the circle in meters.

        Returns:
            The area of the circle in square meters.

        Raises:
            ValueError: If radius is negative.
        '''
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return 3.14159 * radius ** 2

  CLASS docstring:
    class Student:
        '''
        Represents a student in the course.

        Attributes:
            name: The student's full name.
            gpa: The student's current GPA (0.0 to 4.0).
        '''

──────────────────────────────────────────────────────
DRY — DON'T REPEAT YOURSELF
──────────────────────────────────────────────────────
If you find yourself copy-pasting the same code block, STOP.
Extract it into a function and call it wherever you need it.

  ✗ Bad — repeated logic:
    tax_a = price_a * 0.08
    tax_b = price_b * 0.08
    tax_c = price_c * 0.08

  ✓ Good — extracted into a function:
    def calculate_tax(price):
        return price * 0.08

    tax_a = calculate_tax(price_a)
    tax_b = calculate_tax(price_b)
    tax_c = calculate_tax(price_c)

DRY code means: change the tax rate once, in one place, and it
updates everywhere automatically.

──────────────────────────────────────────────────────
MEANINGFUL NAMES
──────────────────────────────────────────────────────
  ✗ Bad:
    def calc(x, y, z):
        return x * y - z

  ✓ Good:
    def calculate_net_price(unit_price, quantity, discount):
        return unit_price * quantity - discount

Avoid single-letter names (except for loop counters: i, j, k).
Avoid abbreviations that aren't universally understood.

──────────────────────────────────────────────────────
COMMENTS — WHEN AND HOW
──────────────────────────────────────────────────────
Good comments explain WHY, not WHAT (the code already shows WHAT).

  ✗ Useless comment (just restates the code):
    x = x + 1   # increment x by 1

  ✓ Useful comment (explains the WHY):
    # Skip the first row because it's a header, not actual data
    for row in data[1:]:

Comment when:
  • The logic is non-obvious or uses a clever trick
  • You're working around a bug or limitation
  • You're citing a formula or algorithm from elsewhere

──────────────────────────────────────────────────────
KEEP FUNCTIONS SMALL AND FOCUSED
──────────────────────────────────────────────────────
Each function should do ONE thing and do it well.
If you need to write "and" to describe what a function does,
consider splitting it into two functions.

  ✗ Does too much:
    def process_user(data):
        # validates, saves to DB, AND sends email

  ✓ Each function has one responsibility:
    def validate_user(data): ...
    def save_user(data): ...
    def send_welcome_email(user): ...

──────────────────────────────────────────────────────
TYPE HINTS — OPTIONAL BUT PROFESSIONAL
──────────────────────────────────────────────────────
Python is dynamically typed, but you can add type hints to make
code clearer:

    def greet(name: str, times: int = 1) -> str:
        return (name + " ") * times

These don't change how the code runs — they're documentation for
developers (and tools like linters and IDEs).

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Refactor code samples to follow best practices.
3. Add docstrings and type hints as directed.
4. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  If you're getting PEP 8 / linting warnings from the editor:
  → Read the warning message — it tells you exactly what to fix.
  → Common fixes: add spaces around operators, shorten long lines,
    rename variables to use snake_case.

Code quality is a craft. The habits you build now will serve you
throughout your entire career. Be proud of clean code! ✨
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all best practices exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
