def grade_average(grade1:int, grade2:int, grade3:int) -> float:
    """
    find out a grade average out of three grades

    >>> grade_average(3,4,5)
    4
    >>> grade_average(5,6,6)
    ?
    """
    return (grade1 + grade2 + grade3) / 3

print(grade_average(3,4,5))
print(grade_average(5,6,6))
