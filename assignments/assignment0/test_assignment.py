# ─────────────────────────────────────────────────────────────────────────────
# Automated tests. You don't edit this file — but READING it shows you exactly
# what your code should do, which is the best way to check your work. Run it from
# the Testing panel (the beaker icon) and aim for all green.
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


def test_hello():
    m = load_student_work()
    # "assert" means "this must be true, or the test fails."
    assert m.hello() == "Hello, world!"
