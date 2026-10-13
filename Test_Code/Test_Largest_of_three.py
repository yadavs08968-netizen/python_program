import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from CODE.largest_of_three import largest_of_three


def test_first_number_largest():
    assert largest_of_three(10, 5, 3) == 10


def test_second_number_largest():
    assert largest_of_three(5, 15, 3) == 15


def test_third_number_largest():
    assert largest_of_three(5, 2, 30) == 30


def test_all_number_equal():
    assert largest_of_three(10, 10, 10) == 10


def test_negative_numbers():
    assert largest_of_three(-5, -2, -10) == -2
