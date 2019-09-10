from typing import Dict

def sparse_add(sp_vector1: Dict, sp_vector2: Dict) -> Dict:
    """takes two sparse vectors stored as dictionaries and
    returns a new dictionary representing their sum
    >>> a = {0: 1, 1: 2, 2: 3}
    >>> b = {0: 4, 1: 5, 2: 6}
    >>> sparse_add(a, b)
    {0: 5, 1: 7, 2: 9}
    >>> c = {0: 6, 1: 5, 2: 4}
    >>> d = {0: 4, 1: 5, 2: 7}
    >>> sparse_add(c, d)
    {0: 10, 1: 10, 2: 11}
    """
    smaller_vector = sp_vector1 if len(sp_vector1) <= len(sp_vector2) else sp_vector2
    summed_vector = sp_vector2 if len(sp_vector1) <= len(sp_vector2) else sp_vector1
    for pos,val in smaller_vector.items():
        if pos in summed_vector:
            summed_vector[pos] += smaller_vector[pos]
        else:
            summed_vector[pos] = smaller_vector[pos]
    return summed_vector

def sparse_dot(sp_vector1: Dict, sp_vector2: Dict) -> int:
    """calculates the dot product of two sparse vectors
    >>> a = {0: 1, 1: 2, 2: 3}
    >>> b = {0: 4, 1: 5, 2: 6}
    >>> sparse_dot(a, b)
    32
    >>> c = {0: 6, 1: 5, 2: 4}
    >>> d = {0: 4, 1: 5, 2: 7, 3: 15}
    >>> sparse_dot(c, d)
    77
    """
    sum = 0
    smaller_vector = sp_vector1 if len(sp_vector1) <= len(sp_vector2) else sp_vector2
    bigger_vector = sp_vector2 if len(sp_vector1) <= len(sp_vector2) else sp_vector1

    for pos,val in smaller_vector.items():
        if pos in bigger_vector:
            sum += smaller_vector[pos] * bigger_vector[pos]
    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()