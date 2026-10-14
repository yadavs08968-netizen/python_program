from CODE.Reverse_Number import reverse_number

def test_reverse_1234():
    assert reverse_number(1234) == 4321

def test_reverse_567():
    assert reverse_number(567) == 765

def test_reverse_120():
    assert reverse_number(120) == 21

def test_reverse_single_digit():
    assert reverse_number(5) == 5

def test_reverse_zero():
    assert reverse_number(0) == 0