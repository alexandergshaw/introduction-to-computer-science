import importlib.util
from pathlib import Path


def load_student_work():
    module_path = Path(__file__).with_name("student_work.py")
    spec = importlib.util.spec_from_file_location("student_work", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_exam2():
    m = load_student_work()
    assert m.Car("Toyota", "Corolla").describe() == "Toyota Corolla"
    assert m.Dog().speak() == "Woof!"
    assert isinstance(m.Dog(), m.Animal)
    assert m.safe_divide(6, 2) == 3
    assert m.safe_divide(1, 0) is None
    assert m.add(2, 3) == 5
