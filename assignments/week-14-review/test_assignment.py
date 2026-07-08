# ─────────────────────────────────────────────────────────────────────────────
# Automated tests. You don't edit this file — but READING it shows you exactly
# what each function should do. Run it from the Testing panel; aim for all green.
# ─────────────────────────────────────────────────────────────────────────────
import importlib.util
from pathlib import Path


def load_student_work():
    """Load your student_work.py so the tests can call your functions."""
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_bank_account():
    m = load_student_work()
    acct = m.BankAccount()          # starts at 0
    assert acct.balance == 0
    acct.deposit(100)               # +100
    acct.withdraw(30)               # -30
    assert acct.balance == 70
    assert m.BankAccount(50).balance == 50   # opening balance


def test_safe_divide():
    m = load_student_work()
    assert m.safe_divide(6, 2) == 3
    assert m.safe_divide(1, 0) is None


def test_is_palindrome():
    m = load_student_work()
    assert m.is_palindrome("racecar") is True
    assert m.is_palindrome("hello") is False
