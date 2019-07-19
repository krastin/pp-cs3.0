def mystery_function(values):
    """This is a mystery function that takes a nested list and creates a new
    list that has the sublist element reversed in order

    mystery_function([[1,2],[3,4,5],[6,7,8,9]])
    >>> [[2, 1], [5, 4, 3], [9, 8, 7, 6]]
    """
    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)
    return result