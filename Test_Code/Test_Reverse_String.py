
from CODE.Reverse_String import reverse_string

def test_reverse_hello():
    assert reverse_string("hello") == "olleh"

def test_reverse_python():
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    assert reverse_string("") == ""

def test_reverse_single_character():
    assert reverse_string("A") == "A"

def test_reverse_number_string():
    assert reverse_string("1234") == "4321"
