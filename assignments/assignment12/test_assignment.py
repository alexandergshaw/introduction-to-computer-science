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


def test_clamp():
    m = load_student_work()
    assert m.clamp(5, 0, 10) == 5     # already inside 0..10
    assert m.clamp(-3, 0, 10) == 0    # below the range -> snaps up to 0
    assert m.clamp(99, 0, 10) == 10   # above the range -> snaps down to 10
