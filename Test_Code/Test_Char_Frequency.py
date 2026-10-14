from CODE.Char_Frequency import count_frequency

def test_frequency_a():
    assert count_frequency("banana", "a") == 3

def test_frequency_n():
    assert count_frequency("banana", "n") == 2

def test_frequency_not_found():
    assert count_frequency("hello", "z") == 0

def test_frequency_empty_string():
    assert count_frequency("", "a") == 0

def test_frequency_case_sensitive():
    assert count_frequency("Apple", "p") == 2
