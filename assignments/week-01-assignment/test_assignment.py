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


def test_greet():
    m = load_student_work()
    assert m.greet("Sam") == "Hello, Sam!"
    assert m.greet("Ada") == "Hello, Ada!"


def test_loud():
    m = load_student_work()
    assert m.loud("hi") == "HI"
    assert m.loud("Wow") == "WOW"


def test_add_excitement():
    m = load_student_work()
    assert m.add_excitement("go") == "go!"
