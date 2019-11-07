from typing import List

def bubble_sort_2(L: list) -> List:
    """Start from the end.
    Take an item and compare it with the previous one, and swap if the former is smaller.
    Keep going until the end of the list.
    Repeat X times the length of the list
    >>> bubble_sort_2([])
    []
    >>> bubble_sort_2([1])
    [1]
    >>> bubble_sort_2([2, 1])
    [1, 2]
    >>> bubble_sort_2([1, 2])
    [1, 2]
    >>> bubble_sort_2([3, 4, 7, -1, 2, 5])
    [-1, 2, 3, 4, 5, 7]
    >>> bubble_sort_2([3, 3, 3])
    [3, 3, 3]
    >>> bubble_sort_2([-5, 3, 0, 3, -6, 2, 1, 1])
    [-6, -5, 0, 1, 1, 2, 3, 3]
    """
    if len(L) < 2:
        return L

    output = L
    swap_happened = True

    while swap_happened:
        current_element = len(output) - 1
        swap_happened = False
        while current_element >= 1:
            if output[current_element] < output[current_element - 1]:
                # swap current element with the next one
                tmp = output[current_element - 1]
                output[current_element - 1] = output[current_element]
                output[current_element] = tmp
                swap_happened = True
            current_element = current_element - 1
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()