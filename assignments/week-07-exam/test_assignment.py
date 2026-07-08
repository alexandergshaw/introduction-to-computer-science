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


def test_letter_grade():
    m = load_student_work()
    assert m.letter_grade(95) == "A"
    assert m.letter_grade(85) == "B"
    assert m.letter_grade(72) == "C"
    assert m.letter_grade(65) == "D"
    assert m.letter_grade(40) == "F"


def test_average():
    m = load_student_work()
    assert m.average([2, 4, 6]) == 4


def test_count_positives():
    m = load_student_work()
    assert m.count_positives([-1, 2, 0, 5]) == 2
    assert m.count_positives([-3, -2]) == 0
