"""
Exam 15 — Exam 2
================
Practice exam covering Weeks 8–13 (classes, inheritance, error handling) plus a
little earlier material. Four short problems at the same level as the weekly work.

Write each one so it matches the description, then run test_assignment.py until
all the tests pass.

What to build:
  1. Car(make, model) — remembers a make and a model.
       .describe() returns them joined by a single space, e.g.  Toyota Corolla
  2. Dog(Animal)      — a subclass of Animal whose speak() returns  Woof!
  3. safe_divide(a, b)-> a divided by b, or None when b is 0
  4. add(a, b)        -> the sum of a and b

Concepts you'll use:
  • Store values on  self  in __init__, then use them inside a method.
  • A subclass (class Dog(Animal)) can override a method to change its behaviour.
  • try / except handles an error instead of letting it crash the program.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


class Car:
    """A car that can describe itself."""

    def __init__(self, make: str, model: str) -> None:
        """Remember this car's make and model for later."""
        self.make = make
        self.model = model

    def describe(self) -> str:
        """
        Return the make and model joined by a single space.

        Example:
            Car("Toyota", "Corolla").describe() -> "Toyota Corolla"
        """
        return f"{self.make} {self.model}"


class Animal:
    """A generic animal. Subclasses override speak() with their own sound."""

    def speak(self) -> str:
        """The default sound; subclasses replace this with their own."""
        return "..."


class Dog(Animal):
    """A dog: a kind of Animal that overrides speak() with its own sound."""

    def speak(self) -> str:
        """Return a dog's sound.  Example: Dog().speak() -> "Woof!" """
        return "Woof!"


def safe_divide(a: float, b: float):
    """
    Return a divided by b. If b is 0, return None instead of crashing.

    Example:
        safe_divide(6, 2) -> 3
        safe_divide(1, 0) -> None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def add(a: float, b: float) -> float:
    """
    Return the sum of a and b.

    Example:
        add(2, 3) -> 5
    """
    return a + b
