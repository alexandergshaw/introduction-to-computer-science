"""
Assignment 04 — Functions and Modular Programming
=================================================
Week 4: parameters, return values, and DEFAULT parameter values.

Problems:
  1. add(a, b, c=0)               -> sum of the numbers (c is optional)
  2. greet(name, greeting="Hello")-> "<greeting>, <name>!" (greeting is optional)
  3. triple(n)                    -> n times 3

Things to know:
  • Writing  c=0  or  greeting="Hello"  gives a parameter a DEFAULT value,
    used when the caller leaves that argument out.

Hint (no spoilers): #1 adds all three; if c is left off it's 0, so it doesn't
change the total. #2 uses greeting in the same spot as Assignment 01's greet.
"""


def add(a: float, b: float, c: float = 0) -> float:
    """Return a + b + c (c is optional, defaults to 0)."""
    return a + b + c


def greet(name: str, greeting: str = "Hello") -> str:
    """Return "<greeting>, <name>!" (greeting defaults to "Hello")."""
    return f"{greeting}, {name}!"


def triple(n: float) -> float:
    """Return n times 3."""
    return n * 3
