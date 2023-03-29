"""EXO7 - Dictionary Functions."""
__author__ = "730576293"

#3 tests ea

def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Given a dict[str, str] returns the same type with keys and values reversed"""
    new_dict: dict[str, str] = dict()
    for key in input_dict:
        if input_dict[key] in new_dict:
            raise KeyError("Duplicate values in dictionary")
        new_dict[input_dict[key]] = key
    return(new_dict)
    

def favorite_color(input_dict: dict[str, str]) -> str:
    """Given a dict[str, str] returns the color(value) str that appears the most & returns the one that appeared first if tied"""
    new_dict: dict[str, int] = dict()
    favorite: list[str, int] = [0, '']
    for name in input_dict:
        if input_dict[name] not in new_dict:
            new_dict[input_dict[name]] = 1
        else: 
            new_dict[input_dict[name]] += 1
    for key in new_dict:
        if new_dict[key] > favorite[0]:
            favorite = [new_dict[key], key]
    return favorite[1]


def count(input_list: list[str]) -> dict[str, int]:
    """Given a list[str] returns dict[str, int] where each key is unique value in given list and value is the count of the number of times that value appeared in the input list."""
    new_dict: dict[str, int] = dict()
    for word in input_list:
        if word not in new_dict:
            new_dict[word] = 1
        else: 
            new_dict[word] += 1
    return new_dict