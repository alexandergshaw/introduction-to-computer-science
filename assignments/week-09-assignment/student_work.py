"""
Assignment 09 — Advanced OOP
============================
Week 9: inheritance and overriding. There is one base class, Animal, and three
specific animals that each inherit from it. Every subclass overrides speak() so
it returns that animal's own sound.

── ASSIGNMENT INSTRUCTIONS (what you must do) ──
Write each subclass so its speak() returns the right sound, then run
test_assignment.py until all the tests pass.

What to build (each one is a subclass of Animal):
  1. Dog — speak() returns  Woof!
  2. Cat — speak() returns  Meow!
  3. Cow — speak() returns  Moo!

── HELPFUL EXAMPLES & NOTES (background — not required steps) ──
Concepts you'll use:
  • Writing  class Dog(Animal)  means "a Dog is a kind of Animal" and inherits
    everything Animal already has.
  • "Overriding" means defining speak() again inside the subclass so it behaves
    differently from the version on Animal.

Tip: open test_assignment.py to see the exact expected sounds.
"""


class Animal:
    """A generic animal. Each subclass overrides speak() with its own sound."""

    def speak(self) -> str:
        """The default sound; subclasses replace this with their own."""
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        """Return a dog's sound.  Helpful example: Dog().speak() -> "Woof!" """
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        """Return a cat's sound.  Helpful example: Cat().speak() -> "Meow!" """
        return "Meow!"


class Cow(Animal):
    def speak(self) -> str:
        """Return a cow's sound.  Helpful example: Cow().speak() -> "Moo!" """
        return "Moo!"
