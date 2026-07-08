"""
Review 14 — Review 2
====================
A mixed review of Weeks 8–13: a class, error handling, and a testing-friendly
function. You've built each of these kinds of things before.

Write each one so it matches the description, then run test_assignment.py until
all the tests pass.

What to build:
  1. BankAccount(balance=0) — a class that remembers a balance (starting at 0
     when no opening balance is given). It has:
       .deposit(amount)  — increases the balance by amount
       .withdraw(amount) — decreases the balance by amount
  2. safe_divide(a, b) -> a divided by b, or None when b is 0       (error handling)
  3. is_palindrome(s)  -> True if s reads the same backwards,
                          ignoring capitalisation                   (testing)

Concepts you'll use:
  • A class keeps its state on  self  (here, self.balance) and its methods change
    that state.
  • try / except handles an error (such as dividing by zero) instead of crashing.
  • A string's  .lower()  copy and its reverse (the  [::-1]  slice) help compare
    a string with itself.

Tip: open test_assignment.py to see the exact inputs and expected outputs.
"""


class BankAccount:
    """A minimal bank account that tracks a balance."""

    def __init__(self, balance: float = 0) -> None:
        """Remember the opening balance (defaults to 0 when none is given)."""
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Increase the account's balance by amount."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Decrease the account's balance by amount."""
        self.balance -= amount


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


def is_palindrome(s: str) -> bool:
    """
    Return True if s reads the same forwards and backwards, ignoring
    capitalisation; otherwise False.

    Example:
        is_palindrome("racecar") -> True
        is_palindrome("hello")   -> False
    """
    cleaned = s.lower()
    return cleaned == cleaned[::-1]
