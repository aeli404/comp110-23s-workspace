"""EXO4 - List Utils"""
__author__ = "730576293"


"""Checks for the presence of an integer in a list of ints, returns a bool"""
def all(int_list = list,check_int = int) -> bool:
  i = 0
  while i < len(int_list):
    if check_int == int_list[i]:
      i += 1
    else:
      return False
  return True


"""Returns the largest integer given a list of ints"""
def max(int_list = list) -> int:
  if len(int_list) == 0:
    raise ValueError("max() arg is an empty List")
  i = 0
  max = int_list[0]
  while i < len(int_list):
    if max < int_list[i]:
      max = int_list[i]
    i += 1
  return max



"""Determines if two lists of ints are equal, will return false for length as well"""
def is_equal(list1 = list, list2 = list) -> bool:
  if len(list1) != len(list2):
    return False
  else:
    i=0
    while i < len(list1):
      if list1[i] != list2[i]:
        return False
      else:
        i += 1
    return True