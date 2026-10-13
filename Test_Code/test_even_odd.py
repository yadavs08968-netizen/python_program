
import importlib.util
from pathlib import Path

# Find the project root folder
root = Path(__file__).resolve().parent.parent

# Get the file path from CODE folder
file_path = root / "CODE" / "even_odd.py"

print("File path is:", file_path)

# Load the Python file
spec = importlib.util.spec_from_file_location(
    "even_odd_module", file_path
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

even_odd = module.even_odd


def test_even_odd_2():
    assert even_odd(2) == "Even"


def test_even_odd_4():
    assert even_odd(4) == "Even"


def test_even_odd_7():
    assert even_odd(7) == "Odd"


def test_even_odd_9():
    assert even_odd(9) == "Odd"


def test_even_odd_0():
    assert even_odd(0) == "Even"


def test_even_odd_11():
    assert even_odd(11) == "Odd"


def test_even_odd_100():
    assert even_odd(100) == "Even"
