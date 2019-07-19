from typing import List

def remove_neg(num_list: List[float]) -> None:
    """Remove the negative numbers from the list num_list.
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """
    for item in range(0, len(num_list)):
        if item >= len(num_list):
            break
        while num_list[item] < 0:
            num_list.remove(num_list[item])

numbers = [1, 2, 3, -3, 6, -1, -3, 1]
print(numbers)
remove_neg(numbers)
print(numbers)