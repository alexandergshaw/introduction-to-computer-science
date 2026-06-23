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


def test_is_palindrome():
    m = load_student_work()
    assert m.is_palindrome("racecar") is True
    assert m.is_palindrome("hello") is False


def test_is_even():
    m = load_student_work()
    assert m.is_even(4) is True
    assert m.is_even(7) is False


def test_absolute():
    m = load_student_work()
    assert m.absolute(-5) == 5
    assert m.absolute(3) == 3
    assert m.absolute(0) == 0
