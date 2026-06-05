"""
Student Work — Exam 15: Exam Practice 2
========================================
Week 15 is Exam Practice 2 — preparation for the second (and final!)
exam of the semester. This exam covers everything from Weeks 8–13,
with some integration of earlier concepts.

──────────────────────────────────────────────────────
WHAT THE EXAM COVERS
──────────────────────────────────────────────────────
  ✓ OOP: Classes, __init__, self, instance methods, attributes
  ✓ Inheritance: parent/child classes, super(), method overriding
  ✓ Polymorphism: same interface, different behavior
  ✓ Error Handling: try/except/else/finally, raise, exception types
  ✓ File I/O: open(), reading, writing, "with" statement
  ✓ Unit Testing: assert, pytest patterns, edge cases
  ✓ Git: commit workflow, branching, merging
  ✓ Best Practices: PEP 8, docstrings, DRY, naming

  PLUS (from Weeks 1–7):
  ✓ Variables, data types, operators
  ✓ Control flow: if/elif/else, loops
  ✓ Functions: parameters, return values, scope
  ✓ Data structures: list, dict, tuple, set

──────────────────────────────────────────────────────
PRACTICE PROBLEMS — TRY THESE WITHOUT HELP
──────────────────────────────────────────────────────
  1. Write a class Vehicle with attributes make, model, year, and
     a method describe() that prints a sentence about the vehicle.
     Then create a class ElectricVehicle that inherits from Vehicle
     and adds a battery_range attribute.

  2. Write a function safe_divide(a, b) that returns a / b, but
     handles ZeroDivisionError gracefully by returning None.

  3. Write a function read_lines(filename) that reads a text file
     and returns a list of lines. Handle FileNotFoundError.

  4. Write two unit tests for safe_divide():
       - One that checks a normal division
       - One that checks division by zero returns None

  5. Trace this code — what does it print?
       class Animal:
           def speak(self):
               return "..."
       class Dog(Animal):
           def speak(self):
               return "Woof!"
       class Cat(Animal):
           def speak(self):
               return "Meow!"
       animals = [Dog(), Cat(), Animal()]
       for a in animals:
           print(a.speak())

──────────────────────────────────────────────────────
EXAM STRATEGY
──────────────────────────────────────────────────────
  1. READ every question carefully before starting.
  2. For tracing problems, step through code line by line on paper.
  3. For writing-code problems, write a plan in comments first.
  4. Start with the questions you're most confident about.
  5. Leave time at the end to review your answers.
  6. If stuck on a question, move on and come back to it.

──────────────────────────────────────────────────────
FINAL REVIEW CHECKLIST
──────────────────────────────────────────────────────
  □ I can define a class with attributes and methods
  □ I can create subclasses that inherit and extend a parent
  □ I can write try/except blocks for specific exception types
  □ I can read and write files safely with "with open(...)"
  □ I can write pytest unit tests using assert
  □ I know the basic Git commit/push/branch workflow
  □ I can write PEP 8-compliant code with good names and docstrings

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for the specific exam practice exercises.
2. Complete each exercise fully.
3. When done, change MODULE_COMPLETED to True.

You have come SO far this semester. Trust your preparation and give
it your best shot. You've got this! 🎯
"""

# ─── Completion Flag ──────────────────────────────────────────────────────────
#
# Change False to True after completing all exam practice exercises.
#
MODULE_COMPLETED = False


# ─── Status Function ──────────────────────────────────────────────────────────
# Do NOT change this function.
#
def module_status() -> bool:
    """Return module completion state."""
    return MODULE_COMPLETED
