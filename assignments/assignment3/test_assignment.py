import importlib.util
from pathlib import Path


def load_student_work():
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_classify():
    m = load_student_work()
    assert m.classify(5) == "positive"
    assert m.classify(-2) == "negative"
    assert m.classify(0) == "zero"
