"""
Assignment 9 — Advanced OOP
===========================
Week 9: inheritance, method overriding, and polymorphism.

Exercise: Dog inherits from Animal and replaces (overrides) speak().
  Animal().speak() -> "..."      Dog().speak() -> "Woof!"

Things to know:
  • Writing  class Dog(Animal)  means "a Dog is a kind of Animal" — it
    inherits everything Animal has.
  • "Overriding" means defining a method again in the child class to change
    what it does.

Hint (no spoilers): give Dog its own speak() that returns the dog's sound;
that quietly replaces the one it inherited from Animal.
"""


class Animal:
    """A generic animal."""

    def speak(self) -> str:
        # The base sound. Subclasses can replace this with their own.
        return "..."


class Dog(Animal):  # Dog is an Animal (it inherits from it)
    """A dog, which makes its own sound."""

    def speak(self) -> str:
        # This speak() OVERRIDES Animal.speak() just for dogs.
        return "Woof!"
