"CQ04 Dictionary Practice."
__author__ = "730576293"

def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Given 2 lists, produces a dictonary where obects in list 1 are the keys and
    objects list 2 are the values"""
    zip_dict: dict = {}
    if len(keys) != len(values) or len(keys) == 0 or len(values) == 0:
        return zip_dict
    for elem in range(0, len(keys)):
        zip_dict[keys[elem]] = values[elem]
    return zip_dict
