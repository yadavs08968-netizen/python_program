
from CODE.Palindrome_String import is_palindrome

def test_palindrome_madam():
    assert is_palindrome("madam") == True

def test_palindrome_level():
    assert is_palindrome("level") == True

def test_not_palindrome_hello():
    assert is_palindrome("hello") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True
