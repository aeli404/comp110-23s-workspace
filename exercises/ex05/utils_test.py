"""EXO5 - 'list' Utility Functions part 2"""
__author__ = "730576293"

from exercises.ex05.utils import only_evens, sub, concat

def test_empty() -> None:
    """Tests empty list input"""
    assert only_evens([]) == []

def test_returnempty() -> None:
    """Tests correct empty list output after given a non-empty list"""
    test_list = [41]
    assert only_evens(test_list) == []

def test_multiple() -> None:
    """Tests list with multiple entries"""
    test_list = [5, 10, 15, 20, 25, 30, 35]
    assert only_evens(test_list) == [10, 20, 30]


def test_sequence() -> None:
    """Tests lists are in the correct order in the output"""
    test_list1 = [2, 4, 6, 8]
    test_list2 = [1, 3, 5, 7]
    assert concat(test_list1, test_list2) == [2, 4, 6, 8, 1, 3, 5, 7]

def test_length() -> None:
    """Tests output list is the correct length for inputs"""
    test_list1 = [2, 4, 6, 8]
    test_list2 = [1, 3, 5, 7]
    test_list3 = concat(test_list1, test_list2)
    assert len(test_list1) + len(test_list2) == len(test_list3)

def test_type() -> None:
    """Tests output given empty first list"""
    test_list1 = []
    test_list2 = [1, 3, 5, 7]
    assert concat(test_list1, test_list2) == [1, 3, 5, 7]


def test_negative_start() -> None:
    """Tests output given a negative start input"""
    test_list = [2, 4, 6, 8, 1, 3, 5, 7]
    assert sub(test_list, -8, 5) == [2, 4, 6, 8, 1]

def test_end_index() -> None:
    """Tests end index is not inculsive"""
    test_list = [10, 20, 30, 40]
    assert sub(test_list, 1, 3) == [20, 30]

def test_empty2() -> None:
    """Tests empty list input"""
    assert sub([], 0, 0) == []