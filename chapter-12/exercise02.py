from typing import List, Tuple

def min_index(L: list) -> Tuple[int, int]:
    """that takes one parameter (a list) and returns a tuple containing
    the minimum value in the list and that value’s index in the list
    >>> min_index([5, 4, 3, 2, 8, 9])
    (2, 3)
    """
    # find both the minimum value in a list and that value’s index
    # in one pass through the list
    smallest = L[0]
    smallest_pos = 0
    for element in L:
        if element < smallest:
            smallest = element
            smallest_pos = L.index(element)
    return (smallest, smallest_pos)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

def min_or_max_index(L: list, minimum: bool) -> Tuple[int, int]:
    """ If the Boolean parameter refers to True
    the function returns a tuple containing the minimum and its index;
    if it refers to False,
    it returns a tuple containing the maximum and its index
    >>> min_or_max_index([5, 4, 3, 2, 8, 9], True)
    (2, 3)
    >>> min_or_max_index([5, 4, 3, 2, 8, 9], False)
    (9, 5)
    """
    # find both the minimum value in a list and that value’s index
    # and the maximum value in a list and that value’s index
    # in one pass through the list
    smallest = L[0]
    smallest_pos = 0
    biggest = L[0]
    biggest_pos = 0
    for element in L:
        if element < smallest:
            smallest = element
            smallest_pos = L.index(element)
        if element > biggest:
            biggest = element
            biggest_pos = L.index(element)            
    if minimum:
        return (smallest, smallest_pos)
    else:
        return (biggest, biggest_pos)


if __name__ == "__main__":
    import doctest
    doctest.testmod()