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


def test_car():
    m = load_student_work()
    assert m.Car("Toyota", "Corolla").describe() == "Toyota Corolla"


def test_dog():
    m = load_student_work()
    assert m.Dog().speak() == "Woof!"
    assert isinstance(m.Dog(), m.Animal)   # inheritance


def test_safe_divide():
    m = load_student_work()
    assert m.safe_divide(6, 2) == 3
    assert m.safe_divide(1, 0) is None


def test_add():
    m = load_student_work()
    assert m.add(2, 3) == 5
