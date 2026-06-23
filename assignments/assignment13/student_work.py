"""
Assignment 13 — Best Practices
==============================
Week 13: clean, readable string helpers. Three small problems.

Problems:
  1. format_full_name(first, last) -> "First Last" with stray spaces trimmed
  2. initials(first, last)         -> uppercase initials, e.g. "Ada","Lovelace" -> "A.L."
  3. slugify(text)                 -> lowercase, trimmed, spaces -> dashes
                                      e.g. "  Hello World " -> "hello-world"

Things to know:
  • .strip() trims surrounding spaces; .lower()/.upper() change case.
  • text[0] is the first character; .replace(" ", "-") swaps spaces for dashes.

Hint (no spoilers): build initials from the first letter of each name; slugify
strips, lowercases, then replaces spaces with dashes.
"""


def format_full_name(first: str, last: str) -> str:
    """Return a tidy 'First Last' string."""
    return f"{first.strip()} {last.strip()}"


def initials(first: str, last: str) -> str:
    """Return uppercase initials like 'A.L.'."""
    # first[0] is the first letter; .upper() makes it a capital.
    return f"{first[0].upper()}.{last[0].upper()}."


def slugify(text: str) -> str:
    """Return a url-friendly slug: lowercase, trimmed, spaces -> dashes."""
    return text.strip().lower().replace(" ", "-")
