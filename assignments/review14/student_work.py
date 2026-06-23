"""
Student Work — Review 14: Review Module 2
==========================================
Week 14 is the second review week — a dedicated opportunity to
consolidate your learning from Weeks 8 through 13, plus a cumulative
pass over Weeks 0–7, before the final exam.

──────────────────────────────────────────────────────
TOPICS TO REVIEW
──────────────────────────────────────────────────────
Use this week to revisit and solidify your understanding of:

  WEEK 8 — OOP: Classes
    □ Defining a class with class ClassName:
    □ The __init__ constructor and the self parameter
    □ Instance attributes vs class attributes
    □ Instance methods
    □ Creating and using objects (instances)

  WEEK 9 — Advanced OOP
    □ Inheritance: child class extends parent class
    □ super().__init__() — calling the parent constructor
    □ Method overriding — redefining a parent's method in a child
    □ Polymorphism — same method name, different behavior per class
    □ Encapsulation — _protected and __private conventions
    □ Abstract base classes (ABC) and @abstractmethod

  WEEK 10 — Error Handling and File I/O
    □ try / except / else / finally
    □ Common exception types: ValueError, TypeError, IndexError, etc.
    □ raise — throwing exceptions intentionally
    □ Opening, reading, and writing files with open() and "with"
    □ File modes: "r", "w", "a"

  WEEK 11 — Unit Testing
    □ What a unit test is and why we write them
    □ pytest: test functions start with test_
    □ assert statements
    □ Testing edge cases
    □ pytest.raises() for testing expected exceptions
    □ The TDD cycle: Red → Green → Refactor

  WEEK 12 — Advanced Unit Testing
    □ Fixtures for reusable setup (@pytest.fixture, tmp_path)
    □ Parametrization (@pytest.mark.parametrize)
    □ Mocking / monkeypatch to isolate code under test
    □ The Arrange–Act–Assert structure
    □ Measuring coverage (pytest --cov)

  WEEK 13 — Best Practices
    □ PEP 8 naming conventions (snake_case, PascalCase, UPPER_CASE)
    □ Docstrings (module, function, class)
    □ DRY: Don't Repeat Yourself
    □ Meaningful variable and function names
    □ Comments explain WHY, not WHAT
    □ Single responsibility principle for functions

  CUMULATIVE — also on Exam 2 (from Weeks 0–7; see Review 1)
    □ Git & GitHub workflow: branching off main, commits, PRs, merging
    □ Python basics: running files, print(), comments, reading errors
    □ Variables & data types; operators; if/elif/else and loops
    □ Functions: parameters, return values, scope
    □ Data structures: list, dict, tuple, set

──────────────────────────────────────────────────────
SELF-TEST QUESTIONS
──────────────────────────────────────────────────────
Try answering these without looking anything up:

  1. What keyword defines a class? What keyword is used for inheritance?
  2. Why must every instance method have "self" as its first parameter?
  3. What does super() do? When would you use it?
  4. What is the difference between "w" and "a" file modes?
  5. What makes a good unit test? Name three characteristics.
  6. What is a pytest fixture, and when would you use one?
  7. How does @pytest.mark.parametrize reduce duplicated test code?
  8. What does DRY mean? Give an example of a DRY violation and how to fix it.

──────────────────────────────────────────────────────
REVIEW STRATEGY
──────────────────────────────────────────────────────
  1. For each week above, open your student_work.py and re-read
     the comments (the reference material is right there!).
  2. Try to re-implement examples from memory.
  3. Focus most of your time on topics where you feel least confident.
  4. The best preparation is writing code — not just reading it.

──────────────────────────────────────────────────────
YOUR TASK
──────────────────────────────────────────────────────
1. Read INSTRUCTIONS.md for any specific review exercises.
2. Complete those exercises.
3. When finished, change MODULE_COMPLETED to True.

The final exam and the final project are just around the corner.
You've learned so much — this review will tie it all together! 🎓
"""

# ─── Exercise solution ──────────────────────────────────────────────────────
class BankAccount:
    """A minimal bank account."""

    def __init__(self, balance: float = 0) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add amount to the balance."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Subtract amount from the balance."""
        self.balance -= amount
