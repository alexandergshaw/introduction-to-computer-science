import importlib.util
from pathlib import Path


def load_student_work():
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_letter_grade():
    m = load_student_work()
    assert m.letter_grade(95) == "A"
    assert m.letter_grade(85) == "B"
    assert m.letter_grade(72) == "C"
    assert m.letter_grade(65) == "D"
    assert m.letter_grade(40) == "F"
