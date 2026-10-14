
from CODE.Remove_Duplicate import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def test_empty_list():
    assert remove_duplicates([]) == []

def test_all_same_numbers():
    assert remove_duplicates([5, 5, 5]) == [5]

def test_preserve_order():
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
