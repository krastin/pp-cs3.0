from exercise006 import grade_average

def grade_best3_average(grade1:int, grade2:int, grade3:int, grade4:int) -> float:
    """
    Return the average of the best 3 of the 4 grades
    >>> grade_best3_average(20,30,40,50)
    40
    >>> grade_best3_average(50,60,70,80)
    70
    >>> grade_best3_average(80,20,70,90)
    80
    """
    return max(
        grade_average(grade1, grade2, grade3),
        grade_average(grade2, grade3, grade4),
        grade_average(grade3, grade4, grade1),
        grade_average(grade4, grade1, grade2)
        )

print(grade_best3_average(20,30,40,50))
print(grade_best3_average(50,60,70,80))
print(grade_best3_average(80,20,70,90))
