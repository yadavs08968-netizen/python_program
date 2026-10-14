
from CODE.Prime_Number import check_prime

def test_check_prime_7():
    assert check_prime(7) == "Prime"

def test_check_prime_10():
    assert check_prime(10) == "Not Prime"
