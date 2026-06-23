"""
Review 14 — Review 2
====================
A mixed review of Weeks 8–13: classes, error handling, and testing-friendly
functions. Three short problems.

Problems:
  1. BankAccount(balance=0) with .deposit(amount) and .withdraw(amount)  (OOP)
  2. safe_divide(a, b) -> a / b, or None if b is 0                       (error handling)
  3. is_palindrome(s)  -> True if s reads the same backwards             (testing)

Hint (no spoilers): deposit raises the balance, withdraw lowers it;
safe_divide catches the divide-by-zero; a palindrome equals its reverse.
"""


class BankAccount:
    """A minimal bank account that tracks a balance."""

    def __init__(self, balance: float = 0) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add amount to the balance."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Subtract amount from the balance."""
        self.balance -= amount


def safe_divide(a: float, b: float):
    """Return a / b, or None if b is 0."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def is_palindrome(s: str) -> bool:
    """Return True if s is the same backwards (case-insensitive)."""
    cleaned = s.lower()
    return cleaned == cleaned[::-1]
