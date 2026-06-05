import importlib.util
from pathlib import Path


def load_student_work():
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_module_completed_flag():
    module = load_student_work()
    assert hasattr(module, "MODULE_COMPLETED")
    assert module.MODULE_COMPLETED is True


def test_module_status_function_matches_flag():
    module = load_student_work()
    assert hasattr(module, "module_status")
    assert module.module_status() is module.MODULE_COMPLETED
