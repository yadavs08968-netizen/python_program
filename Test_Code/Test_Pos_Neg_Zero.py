
from CODE.Pos_Neg_Zero import pos_neg_zero

def test_positive():
    assert pos_neg_zero(20) == "Positive"

def test_negative():
    assert pos_neg_zero(-10) == "Negative"

def test_zero():
    assert pos_neg_zero(0) == "Zero"
