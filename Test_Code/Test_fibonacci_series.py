
from CODE.Fiboacci_series import fibonacci_series

def test_fibonacci_series_1():
    assert fibonacci_series(1) == [0]

def test_fibonacci_series_2():
    assert fibonacci_series(2) == [0, 1]

def test_fibonacci_series_5():
    assert fibonacci_series(5) == [0, 1, 1, 2, 3]

def test_fibonacci_series_6():
    assert fibonacci_series(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_series_7():
    assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
