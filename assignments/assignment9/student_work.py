"""
Assignment 9 — Advanced OOP
===========================
Week 9: inheritance, method overriding, and polymorphism.

Exercise: Dog inherits from Animal and overrides speak().
  Animal().speak() -> "..." ; Dog().speak() -> "Woof!"
"""


class Animal:
    """Base animal."""

    def speak(self) -> str:
        """The generic animal sound."""
        return "..."


class Dog(Animal):
    """A dog overrides speak()."""

    def speak(self) -> str:
        return "Woof!"
