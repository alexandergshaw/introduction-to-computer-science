import importlib.util
from pathlib import Path


def load_student_work():
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_clamp():
    m = load_student_work()
    assert m.clamp(5, 0, 10) == 5
    assert m.clamp(-3, 0, 10) == 0
    assert m.clamp(99, 0, 10) == 10
