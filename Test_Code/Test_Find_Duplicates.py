from CODE.Find_Duplicates import find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 4, 2, 5, 3]) == [2, 3]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == []


def test_all_duplicates():
    assert find_duplicates([1, 1, 2, 2]) == [1, 2]


def test_multiple_occurrences():
    assert find_duplicates([1, 1, 1, 2, 2, 3]) == [1, 2]


def test_empty_list():
    assert find_duplicates([]) == []
