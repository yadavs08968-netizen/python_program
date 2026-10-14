
from CODE.Prime_In_Range import prime_number

def test_prime_range_10():
    assert prime_number(1, 10) == [2, 3, 5, 7]

def test_prime_range_20():
    assert prime_number(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_no_prime():
    assert prime_number(8, 10) == []

def test_single_prime():
    assert prime_number(13, 13) == [13]

def test_negative_range():
    assert prime_number(-10, 10) == [2, 3, 5, 7]
