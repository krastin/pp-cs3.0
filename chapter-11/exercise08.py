from typing import Dict

def is_balanced(color: Dict) -> bool:
    """takes a dictionary whose keys are 'R', 'G', and 'B'
    and whose values are between 0 and 1 as input
    and returns True if they add up to 1.0
    >>> is_balanced({'R': 0.2, 'G': 0.6, 'B': 0.2})
    True
    >>> is_balanced({'R': 0.6, 'G': 0.6, 'B': 0.2})
    False
    >>> is_balanced({'R': 0.1, 'G': 0.6, 'B': 0.3})
    True
    """
    values = list(color.values())
    sum = 0.0
    for value in values:
        sum += value
    if sum == 1.0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()