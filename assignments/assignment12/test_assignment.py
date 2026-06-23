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


def test_clamp():
    m = load_student_work()
    assert m.clamp(5, 0, 10) == 5     # already inside the range
    assert m.clamp(-3, 0, 10) == 0    # too low  -> snaps up to 0
    assert m.clamp(99, 0, 10) == 10   # too high -> snaps down to 10


def test_in_range():
    m = load_student_work()
    assert m.in_range(5, 0, 10) is True
    assert m.in_range(15, 0, 10) is False


def test_sign():
    m = load_student_work()
    assert m.sign(7) == 1
    assert m.sign(-7) == -1
    assert m.sign(0) == 0
