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


def test_letter_grade():
    m = load_student_work()
    assert m.letter_grade(95) == "A"   # 90+
    assert m.letter_grade(85) == "B"   # 80s
    assert m.letter_grade(72) == "C"   # 70s
    assert m.letter_grade(65) == "D"   # 60s
    assert m.letter_grade(40) == "F"   # below 60
