# ─────────────────────────────────────────────────────────────────────────────
# Automated tests. You don't edit this file — but READING it shows you exactly
# what your code should do. Run it from the Testing panel and aim for all green.
# ─────────────────────────────────────────────────────────────────────────────
import importlib.util
from pathlib import Path


def load_student_work():
    """Load your student_work.py so the test below can call your functions."""
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_bank_account():
    m = load_student_work()
    acct = m.BankAccount()       # a brand-new account starts at 0
    assert acct.balance == 0
    acct.deposit(100)            # balance goes up by 100
    acct.withdraw(30)            # balance goes down by 30
    assert acct.balance == 70
    assert m.BankAccount(50).balance == 50   # can start with an opening balance
