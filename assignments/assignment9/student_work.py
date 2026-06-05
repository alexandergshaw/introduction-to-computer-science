"""
Student Work — Assignment 9: Advanced OOP
==========================================
Week 9 goes deeper into Object-Oriented Programming with four
core concepts: Inheritance, Polymorphism, Encapsulation, and
Abstraction — often called the "four pillars of OOP."

──────────────────────────────────────────────────────
PILLAR 1: INHERITANCE
──────────────────────────────────────────────────────
Inheritance lets a new class (child) automatically get all the
attributes and methods of an existing class (parent). This means
you don't have to rewrite shared code.

    class Animal:
        'Base class for all animals.'
        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

        def speak(self):
            print(f"{self.name} says {self.sound}!")

    class Dog(Animal):
        'Dog inherits everything from Animal.'
        def fetch(self):
            print(f"{self.name} fetches the ball!")

    class Cat(Animal):
        'Cat also inherits from Animal, adds its own behavior.'
        def purr(self):
            print(f"{self.name} purrs...")

    my_dog = Dog("Buddy", "Woof")
    my_dog.speak()    # Buddy says Woof!  ← inherited from Animal
    my_dog.fetch()    # Buddy fetches the ball!  ← Dog-specific

    my_cat = Cat("Luna", "Meow")
    my_cat.speak()    # Luna says Meow!
    my_cat.purr()     # Luna purrs...

──────────────────────────────────────────────────────
super() — CALLING THE PARENT CLASS
──────────────────────────────────────────────────────
Use super() to call a method from the parent class. Most commonly
used inside __init__ to run the parent's setup code first:

    class GuideDog(Dog):
        def __init__(self, name, owner):
            super().__init__(name, "Woof")  # run Dog/Animal's __init__
            self.owner = owner              # then add our own attribute

        def guide(self):
            print(f"{self.name} guides {self.owner} safely.")

──────────────────────────────────────────────────────
PILLAR 2: POLYMORPHISM
──────────────────────────────────────────────────────
"Polymorphism" means "many forms." It allows objects of different
classes to be used through the same interface — you call the same
method name, but each class does it differently.

    animals = [Dog("Buddy", "Woof"), Cat("Luna", "Meow")]

    for animal in animals:
        animal.speak()   # each animal speaks in its own way!
    # Buddy says Woof!
    # Luna says Meow!

METHOD OVERRIDING — the child class redefines the parent's method:

    class GoldenRetriever(Dog):
        def speak(self):
            # Override Dog's inherited speak() with a custom version
            print(f"{self.name} barks happily!")

──────────────────────────────────────────────────────
PILLAR 3: ENCAPSULATION
──────────────────────────────────────────────────────
Encapsulation means hiding internal details and only exposing what
is necessary. In Python, by convention:

  • Public attributes/methods: accessible everywhere
      self.name

  • "Protected" (single underscore): meant for internal use,
    but still accessible
      self._balance   (convention: "please don't touch this directly")

  • "Private" (double underscore): name-mangled, harder to access
    from outside
      self.__password   (truly hidden — use a method to access it)

Using "getter" and "setter" methods to control access:

    class BankAccount:
        def __init__(self, balance):
            self.__balance = balance    # private

        def get_balance(self):
            return self.__balance       # controlled read access

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount  # controlled write access

──────────────────────────────────────────────────────
PILLAR 4: ABSTRACTION
──────────────────────────────────────────────────────
Abstraction means showing only what's necessary and hiding the
implementation details. Think of a car: you know how to drive it
(steer, accelerate, brake) without knowing how the engine works.

In Python, you can use Abstract Base Classes (ABCs) to define a
"template" that forces subclasses to implement certain methods:

    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass   # subclasses MUST implement this

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14159 * self.radius ** 2

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exercises.
2. Build class hierarchies using inheritance.
3. Override methods and use super() as needed.
4. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "TypeError: Can't instantiate abstract class X with abstract method y"
      → You forgot to implement an @abstractmethod in your subclass.

  ✗ "__init__ not calling super()"
      → If your child class has __init__, call super().__init__(...)
        to properly initialize the parent class too.

  ✗ Unexpected behavior when overriding a method
      → Check whether you want to REPLACE the parent method completely
        or EXTEND it (call super().method() first, then add your code).

OOP at this level is what separates beginners from intermediate programmers.
You're leveling up fast! 🚀
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all advanced OOP exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
