
from CODE.Second_Largest import second_largest

def test_second_largest():
    assert second_largest([10, 20, 30, 40]) == 30

def test_with_duplicates():
    assert second_largest([10, 20, 20, 30]) == 20

def test_negative_numbers():
    assert second_largest([-5, -1, -10]) == -5

def test_same_numbers():
    assert second_largest([5, 5, 5]) is None

def test_single_number():
    assert second_largest([10]) is None
