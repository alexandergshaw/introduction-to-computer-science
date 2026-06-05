"""
Student Work — Assignment 8: OOP Classes
=========================================
Week 8 introduces Object-Oriented Programming (OOP) — one of the
most widely used programming paradigms in the real world.

──────────────────────────────────────────────────────
WHAT IS OBJECT-ORIENTED PROGRAMMING?
──────────────────────────────────────────────────────
OOP is a way of organizing code around "objects" — bundles that
combine DATA (called attributes) and BEHAVIOR (called methods).

Think of it this way:
  • A class is like a BLUEPRINT (e.g., a blueprint for a Car)
  • An object is an INSTANCE created from that blueprint (e.g., your specific car)

You can create many objects from the same class, each with their own data.

──────────────────────────────────────────────────────
DEFINING A CLASS
──────────────────────────────────────────────────────
    class Dog:
        'Represents a dog.'

        def __init__(self, name, breed, age):
            # __init__ is the "constructor" — it runs when you create a new Dog
            self.name = name    # self.name is an ATTRIBUTE
            self.breed = breed
            self.age = age

        def bark(self):
            # bark() is a METHOD — a function that belongs to Dog
            print(self.name + " says: Woof!")

        def describe(self):
            print(f"{self.name} is a {self.age}-year-old {self.breed}.")

──────────────────────────────────────────────────────
CREATING AND USING OBJECTS (INSTANCES)
──────────────────────────────────────────────────────
    # Create instances by calling the class like a function:
    my_dog = Dog("Buddy", "Labrador", 3)
    your_dog = Dog("Bella", "Poodle", 5)

    # Access attributes:
    print(my_dog.name)    # Buddy
    print(your_dog.age)   # 5

    # Call methods:
    my_dog.bark()         # Buddy says: Woof!
    your_dog.describe()   # Bella is a 5-year-old Poodle.

    # Modify attributes:
    my_dog.age = 4        # happy birthday, Buddy!

──────────────────────────────────────────────────────
THE ROLE OF "self"
──────────────────────────────────────────────────────
Every method in a class must have "self" as its FIRST parameter.
"self" refers to the specific object the method is being called on.

When you write:
    my_dog.bark()

Python automatically passes my_dog as the "self" argument. That's
how bark() knows which dog's name to print.

You MUST include self in method definitions, but you do NOT include
it when calling the method.

──────────────────────────────────────────────────────
__init__ — THE CONSTRUCTOR
──────────────────────────────────────────────────────
__init__ (double underscore on each side — called "dunder init") is a
special method that Python automatically calls when you create a new object.

Use it to:
  • Define the object's initial attributes (self.x = ...)
  • Validate or transform the initial values

    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance      # default is $0

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient funds!")
            else:
                self.balance -= amount

        def get_balance(self):
            return self.balance

──────────────────────────────────────────────────────
INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES
──────────────────────────────────────────────────────
  INSTANCE attributes (defined in __init__ with self.):
      → unique to each individual object
      → self.name, self.balance, etc.

  CLASS attributes (defined directly in the class body):
      → shared by ALL objects of that class
      → useful for constants or shared data

    class Dog:
        species = "Canis lupus familiaris"  # class attribute
        def __init__(self, name):
            self.name = name                # instance attribute

──────────────────────────────────────────────────────
WHY USE CLASSES?
──────────────────────────────────────────────────────
  ✓ Group related data and behavior together (encapsulation)
  ✓ Model real-world things naturally (students, accounts, products)
  ✓ Create multiple independent objects from the same template
  ✓ Make code easier to read, test, and maintain
  ✓ Enable inheritance (covered in Week 9!)

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific class-writing exercises.
2. Define your class(es) as described.
3. Create instances and call methods to test your work.
4. When done, change MODULE_COMPLETED to True.

TROUBLESHOOTING
---------------
  ✗ "TypeError: __init__() missing 1 required positional argument"
      → You forgot to pass a required argument when creating the object.

  ✗ "AttributeError: 'Dog' object has no attribute 'name'"
      → You forgot to define self.name inside __init__.

  ✗ "TypeError: bark() takes 1 positional argument but 2 were given"
      → You forgot to add self as the first parameter of the method.

OOP is a paradigm shift — think in THINGS, not just in steps.
Once it clicks, you'll never look back! 🐾
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all OOP/class exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
