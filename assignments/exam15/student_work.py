"""
Exam 15 — Exam 2
================
Practice exam covering Weeks 8–13 (OOP, inheritance, error handling) plus a
little earlier material. Four short problems at the same easy level.

Problems:
  1. Car(make, model) with .describe() -> "<make> <model>"   (class + method)
  2. Dog(Animal).speak() -> "Woof!"                          (inheritance/overriding)
  3. safe_divide(a, b)   -> a / b, or None if b is 0         (error handling)
  4. add(a, b)           -> a + b                            (basics)

Hint (no spoilers): store make/model in __init__ and join them in describe();
Dog inherits from Animal and replaces speak() with its own sound.
"""


class Car:
    """A car that can describe itself."""

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def describe(self) -> str:
        """Return '<make> <model>'."""
        return f"{self.make} {self.model}"


class Animal:
    """A generic animal."""

    def speak(self) -> str:
        return "..."


class Dog(Animal):
    """A dog overrides speak() with its own sound."""

    def speak(self) -> str:
        return "Woof!"


def safe_divide(a: float, b: float):
    """Return a / b, or None if b is 0."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b
