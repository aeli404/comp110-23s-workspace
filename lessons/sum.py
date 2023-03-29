"""Lesson 16 follow-along - lesson function for unit tests"""

def sum(xs: list[float]) -> float:
    """returns sum of all elements in xs"""
    sum_total: float = 0.0
    for elem in range(0,len(xs)):
        sum_total += xs[elem]
    return sum_total

print(sum([24, 5, 75]))