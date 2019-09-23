from typing import Any

def linear_search_while(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    i = 0 # The index of the next item in lst to examine.
    # Keep going until we reach the end of lst or until we find value.
    while i != len(lst) and lst[i] != value:
        i = i + 1
    # If we fell off the end of the list, we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i

def linear_search_for(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def linear_search_sentinel(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    # Add the sentinel.
    lst.append(value)
    i = 0
    # Keep going until we find value.
    while lst[i] != value:
        i = i + 1

    # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i