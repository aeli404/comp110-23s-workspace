"""EXO5 - 'list' Utility Functions."""
__author__ = "730576293"


def only_evens(int_list: list[int]) -> list[int]:
    """Returns a list of the even integers present in the list inputed."""
    evens = []
    for i in int_list:
        if i % 2 == 0:
            evens.append(i)
    return evens


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Returns a list of the values in list1 followed by list 2."""
    concat_list = []
    for i in list1:
        concat_list.append(i)
    for i in list2:
        concat_list.append(i)
    return concat_list


def sub(input_list: list[int], start_input: int, end_input: int) -> list[int]:
    """When input a list and start and stop indexes, returns a new list of the original list vaules within the given indexes."""
    sub_list = []
    if len(input_list) == 0 or start_input >= len(input_list) or end_input <= 0:
        return sub_list
    else:
        if start_input < 0:
            start_i = 0
        else:
            start_i = start_input
        if end_input > len(input_list):
            end_i = len(input_list)
        else:
            end_i = end_input
        for i in range(start_i, end_i):
            sub_list.append(input_list[i])
        return sub_list
