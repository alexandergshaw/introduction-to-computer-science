"""
Assignment 13 — Best Practices
==============================
Week 13: PEP 8, clear names, docstrings, and DRY code.

Exercise: format_full_name(first, last) returns "First Last" with any
surrounding whitespace trimmed.
  format_full_name("  Ada ", "Lovelace") -> "Ada Lovelace"
"""


def format_full_name(first: str, last: str) -> str:
    """Return a clean 'First Last' string."""
    return f"{first.strip()} {last.strip()}"
