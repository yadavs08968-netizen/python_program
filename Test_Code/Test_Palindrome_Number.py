from CODE.Check_Palindrome_Number import Check_palindrome

def test_palindrome_121():
    assert Check_palindrome(121) == "Palindrome"

def test_palindrome_1221():
    assert Check_palindrome(1221) == "Palindrome"

def test_not_palindrome_10():
    assert Check_palindrome(10) == "Not Palindrome"

def test_single_digit():
    assert Check_palindrome(5) == "Palindrome"

def test_zero():
    assert Check_palindrome(0) == "Palindrome"