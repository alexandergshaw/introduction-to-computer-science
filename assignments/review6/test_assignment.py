import importlib.util
from pathlib import Path


def load_student_work():
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_even_numbers():
    m = load_student_work()
    assert m.even_numbers([1, 2, 3, 4]) == [2, 4]
    assert m.even_numbers([1, 3, 5]) == []
