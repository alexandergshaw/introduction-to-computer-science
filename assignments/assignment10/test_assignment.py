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


def test_safe_divide():
    m = load_student_work()
    assert m.safe_divide(6, 2) == 3      # normal division
    assert m.safe_divide(1, 0) is None   # divide-by-zero handled


def test_to_int():
    m = load_student_work()
    assert m.to_int("42") == 42          # a valid number
    assert m.to_int("abc") == 0          # not a number -> default 0
    assert m.to_int("abc", -1) == -1     # custom default


def test_safe_get():
    m = load_student_work()
    assert m.safe_get([10, 20, 30], 1) == 20   # valid index
    assert m.safe_get([10, 20, 30], 9) is None  # out of range -> None
