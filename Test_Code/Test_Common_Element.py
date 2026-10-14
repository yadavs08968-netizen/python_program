from CODE.Common_Element import common_element


def test_common_elements():
    assert common_element([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) == [4, 5]


def test_no_common_elements():
    assert common_element([1, 2], [3, 4]) == []


def test_all_common_elements():
    assert common_element([1, 2], [1, 2]) == [1, 2]


def test_duplicate_elements():
    assert common_element([1, 2, 2, 3], [2, 2, 3]) == [2, 3]


def test_empty_list():
    assert common_element([], [1, 2, 3]) == []