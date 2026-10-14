
from CODE.Sum_Of_Digits import Sum_Of_Digits

def test_sum_123():
    assert Sum_Of_Digits(123) == 6

def test_sum_4567():
    assert Sum_Of_Digits(4567) == 22

def test_sum_zero():
    assert Sum_Of_Digits(0) == 0

def test_sum_negative():
    assert Sum_Of_Digits(-123) == 6

def test_sum_single_digit():
    assert Sum_Of_Digits(5) == 5