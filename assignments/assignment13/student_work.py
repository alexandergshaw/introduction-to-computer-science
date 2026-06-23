"""
Assignment 13 — Best Practices
==============================
Week 13: clean code — clear names, docstrings, and DRY (Don't Repeat Yourself).

Exercise: format_full_name(first, last) returns "First Last" with any extra
spaces around the names removed.
  format_full_name("  Ada ", "Lovelace") -> "Ada Lovelace"

Things to know:
  • .strip() removes spaces from the start and end of a string.
  • An f-string joins pieces of text together, filling in the { } parts.

Hint (no spoilers): trim each name, then join them with a single space between.
"""


def format_full_name(first: str, last: str) -> str:
    """Return a tidy 'First Last' string."""
    # .strip() cleans stray spaces; the single space in "{...} {...}" separates them.
    return f"{first.strip()} {last.strip()}"
