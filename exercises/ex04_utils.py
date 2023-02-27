"""EXO4 - List Utils."""

__author__ = "730576293"


def all(int_list: list[int], check_int: int) -> bool:
    """Checks for the presence of an integer in a list of ints, returns a bool."""
    i = 0
    if len(int_list) == 0:
        return False
    while i < len(int_list):
        if check_int == int_list[i]:
            i += 1
        else:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Returns the largest integer given a list of ints."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    i = 0
    max: int = int_list[0]
    while i < len(int_list):
        if max < int_list[i]:
            max = int_list[i]
        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if two lists of ints are equal, will return false for length as well."""
    if len(list1) != len(list2):
        return False
    else:
        i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        else:
            i += 1
    return True