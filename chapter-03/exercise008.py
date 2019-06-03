from exercise004 import absolute_difference

def weeks_elapsed(day1:int, day2:int) -> int:
    """
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return absolute_difference(day1,day2) // 7

print(weeks_elapsed(3, 20))
print(weeks_elapsed(20, 3))
print(weeks_elapsed(8, 5))
print(weeks_elapsed(40, 61))
