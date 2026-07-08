"""
Assignment 13 — Best Practices
==============================
Week 13: clean, readable string helpers. Three small problems.

Write each function so it matches the description, then run test_assignment.py
until all the tests pass.

What to build:
  1. format_full_name(first, last) -> "<first> <last>" as one string, with any
                                      extra spaces around each name removed
  2. initials(first, last)         -> the uppercase first letters, each followed
                                      by a dot, e.g. "Ada","Lovelace" -> "A.L."
  3. slugify(text)                 -> a tidy, URL-friendly version of text:
                                      lowercase, trimmed, and with spaces turned
                                      into dashes

Concepts you'll use:
  • .strip() removes spaces from the start and end of a string; .lower() and
    .upper() change its case.
  • text[0] is the first character of a string; .replace(old, new) swaps every
    occurrence of one substring for another.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


def format_full_name(first: str, last: str) -> str:
    """
    Return "<first> <last>" as a single string, with any extra spaces around
    each name removed.

    Example:
        format_full_name("Ada", "Lovelace")      -> "Ada Lovelace"
        format_full_name("  Ada ", "Lovelace ")  -> "Ada Lovelace"
    """
    return f"{first.strip()} {last.strip()}"


def initials(first: str, last: str) -> str:
    """
    Return the uppercase initials, each followed by a dot.

    Example:
        initials("Ada", "Lovelace") -> "A.L."
        initials("grace", "hopper")  -> "G.H."
    """
    return f"{first[0].upper()}.{last[0].upper()}."


def slugify(text: str) -> str:
    """
    Return a URL-friendly slug: lowercase, trimmed, with spaces turned into
    dashes.

    Example:
        slugify("  Hello World ") -> "hello-world"
    """
    return text.strip().lower().replace(" ", "-")
