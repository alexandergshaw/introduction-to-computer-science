import importlib.util
from pathlib import Path


def load_student_work():
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_student_name_is_set():
    module = load_student_work()
    assert hasattr(module, "STUDENT_NAME")
    assert isinstance(module.STUDENT_NAME, str)
    assert module.STUDENT_NAME.strip()
    assert module.STUDENT_NAME != "Your Name"
