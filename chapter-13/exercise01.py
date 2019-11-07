from typing import Any

def linear_search_while(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_while([2, 5, 1, -3], 5)
    1
    >>> linear_search_while([2, 4, 2], 2)
    0
    >>> linear_search_while([2, 5, 1, -3], 4)
    -1
    >>> linear_search_while([], 5)
    -1
    """
    last_found_position = -1
    i = len(lst) - 1 # The index of the next item in lst to examine.
    # Keep going until we reach the first of lst or until we find value.
    while i >= 0:
        if lst[i] == value:
            last_found_position = i
        i = i - 1
    # If we fell off the end of the list, we didn't find value.
    return last_found_position

def linear_search_for(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_for([2, 5, 1, -3], 5)
    1
    >>> linear_search_for([2, 4, 2], 2)
    0
    >>> linear_search_for([2, 5, 1, -3], 4)
    -1
    >>> linear_search_for([], 5)
    -1
    """
    last_found_position = -1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            last_found_position = i
    return last_found_position


def linear_search_sentinel(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_sentinel([2, 5, 1, -3], 5)
    1
    >>> linear_search_sentinel([2, 4, 2], 2)
    0
    >>> linear_search_sentinel([2, 5, 1, -3], 4)
    -1
    >>> linear_search_sentinel([], 5)
    -1
    """
    last_found_position = -1
    # Add the sentinel.
    lst.append(value)
    i = len(lst) - 2
    # Keep going until we find value.
    while i >= 0: 
        if lst[i] == value:
            last_found_position = i
        i = i - 1

    # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    return last_found_position


if __name__ == "__main__":
    import doctest
    doctest.testmod()