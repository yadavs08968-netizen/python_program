from CODE.Find_Missing_Number import find_missing


def test_missing_middle_number():
    assert find_missing([1, 2, 4, 5]) == 3


def test_missing_first_number():
    assert find_missing([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert find_missing([1, 2, 3, 4]) == 5


def test_missing_number_from_longer_list():
    assert find_missing([1, 2, 3, 5, 6]) == 4


def test_missing_number_in_two_element_list():
    assert find_missing([1, 3]) == 2
