from CODE.Factorial import Factorial

def test_factorial_5():
    assert Factorial(5) == 120

def test_factorial_4():    
    assert Factorial(4) == 24

def test_factorial_3():    
    assert Factorial(3) == 6

def test_factorial_1():    
    assert Factorial(1) == 1

def test_factorial_0():    
    assert Factorial(0) == 1

print("All test cases passed!")        