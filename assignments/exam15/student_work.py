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
  ✓ Advanced Unit Testing: fixtures, parametrization, mocking, coverage
  ✓ Best Practices: PEP 8, docstrings, DRY, naming

  PLUS (from Weeks 0–7):
  ✓ Git & GitHub workflow: branching off main, commits, pull requests, merging
  ✓ Python basics: running files, print(), comments, reading errors
  ✓ Variables, data types, operators
  ✓ Control flow: if/elif/else, loops
  ✓ Functions: parameters, return values, scope
  ✓ Data structures: list, dict, tuple, set

──────────────────────────────────────────────────────
PRACTICE PROBLEMS — SMALL & GUIDED (fill in the blank, then run to check)
──────────────────────────────────────────────────────
These are intentionally short. Each is only a line or two — together they
touch every topic above without any trick questions.

  1. CLASS + METHOD (OOP)
     Fill in describe() so it prints the make and model:

         class Car:
             def __init__(self, make, model):
                 self.make = make
                 self.model = model
             def describe(self):
                 print(________)        # e.g. prints: Toyota Corolla

         Car("Toyota", "Corolla").describe()

  2. INHERITANCE + POLYMORPHISM
     Write a Dog subclass (1–2 lines) that overrides speak():

         class Animal:
             def speak(self):
                 return "..."

         # class Dog(Animal):  ← you finish this so speak() returns "Woof!"

         print(Dog().speak())           # should print: Woof!

  3. ERROR HANDLING
     Fill in the except so it returns None instead of crashing:

         def safe_divide(a, b):
             try:
                 return a / b
             except ____________:       # which error happens at b = 0?
                 return None

  4. FILE I/O
     Use the safe "with" pattern to print each line of a file:

         with open("notes.txt") as f:
             for line in f:
                 print(line.strip())

  5. UNIT TEST
     Fill in the expected value so the test passes:

         def add(a, b):
             return a + b

         def test_add():
             assert add(2, 3) == ____

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

# ─── Exercise solutions ─────────────────────────────────────────────────────
class Car:
    """A car that can describe itself."""

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def describe(self) -> str:
        """Return 'make model'."""
        return f"{self.make} {self.model}"


class Animal:
    def speak(self) -> str:
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


def safe_divide(a: float, b: float):
    """Return a / b, or None if dividing by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b
