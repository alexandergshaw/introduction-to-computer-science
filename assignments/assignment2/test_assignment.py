import importlib.util
from pathlib import Path


def load_student_work():
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
