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


def test_rectangle_area():
    m = load_student_work()
    assert m.rectangle_area(3, 4) == 12
    assert m.rectangle_area(5, 5) == 25


def test_square():
    m = load_student_work()
    assert m.square(4) == 16
    assert m.square(10) == 100


def test_average():
    m = load_student_work()
    assert m.average(4, 6) == 5
    assert m.average(10, 0) == 5
