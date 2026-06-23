"""
Assignment 09 — Advanced OOP
============================
Week 9: inheritance and overriding. One base class, three animals.

Problems (each subclass overrides speak()):
  1. Dog(Animal).speak() -> "Woof!"
  2. Cat(Animal).speak() -> "Meow!"
  3. Cow(Animal).speak() -> "Moo!"

Things to know:
  • class Dog(Animal)  means "a Dog is a kind of Animal" — it inherits from it.
  • "Overriding" = defining speak() again in the child to change what it says.

Hint (no spoilers): each animal is the same idea — inherit from Animal, then
give it its own speak() that returns its sound.
"""


class Animal:
    """A generic animal."""

    def speak(self) -> str:
        # The base sound; each subclass replaces this with its own.
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


class Cow(Animal):
    def speak(self) -> str:
        return "Moo!"
