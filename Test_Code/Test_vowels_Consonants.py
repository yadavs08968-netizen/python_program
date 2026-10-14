
from CODE.Vowels_consonants import check_vowel_consonant

def test_vowel_a():
    assert check_vowel_consonant("a") == "Vowel"

def test_vowel_uppercase():
    assert check_vowel_consonant("E") == "Vowel"

def test_consonant():
    assert check_vowel_consonant("b") == "Consonant"

def test_invalid_number():
    assert check_vowel_consonant("5") == "Invalid"

def test_invalid_multiple_characters():
    assert check_vowel_consonant("ab") == "Invalid"

def test_invalid_non_ascii():
    assert check_vowel_consonant("é") == "Invalid"
