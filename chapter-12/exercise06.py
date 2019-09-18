# copied from find_two_smallest.py

from typing import Callable, List, Tuple, Any

def find_two_smallest_edit(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest_edit(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    >>> items = [96, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest_edit(items)
    (0, 6)
    >>> items == [96, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    # Find the index of the minimum item in L
    smallest = min(L)
    smallest_pos = L.index(smallest)
    # Remove that item from the list
    L.remove(smallest)
    # Find the index of the new minimum item in the list
    second_smallest = min(L)
    second_smallest_pos = L.index(second_smallest)
    # Put the smallest item back in the list
    L.insert(smallest_pos, smallest)
    # If necessary, adjust the second index
    if smallest_pos <= second_smallest_pos:
        second_smallest_pos += 1
    # Return the two indices
    return (smallest_pos, second_smallest_pos)

def find_two_smallest_copy(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest_copy(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    >>> items = [96, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest_edit(items)
    (0, 6)
    """
    # Sort a copy of L
    array = L.copy()
    array.sort()
    # Get the two smallest numbers
    smallest = array[0]
    second_smallest = array[1]
    # Find their indices in the original list L
    smallest_pos = L.index(smallest)
    second_smallest_pos = L.index(second_smallest)
    # Return the two indices
    return (smallest_pos, second_smallest_pos)
    
def find_two_smallest_walk(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest_walk(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    >>> items = [96, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest_edit(items)
    (0, 6)
    """
    smallest = L[0]
    second_smallest = L[0]
    # Examine each value in the list in order
    for element in L:
        # Keep track of the indices of the two smallest values found so far
        # Update the indices when a new smaller value is found
        if element < smallest:
            second_smallest = smallest
            smallest = element
        elif element > smallest and element < second_smallest:
            second_smallest = element
    # Return the two indices
    return (L.index(smallest), L.index(second_smallest))

if __name__ == "__main__":
    import doctest
    doctest.testmod()