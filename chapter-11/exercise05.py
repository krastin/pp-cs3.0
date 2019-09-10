from typing import Dict

def count_values(sample_dict: Dict) -> int:
    """takes a single dictionary as an argument and returns the number of distinct values it contains
    >>> sample_dict = {'red': 1, 'green': 1, 'blue': 2}
    >>> count_values(sample_dict)
    2
    """
    unique_values = []
    for k,v in sample_dict.items():
        if v not in unique_values:
            unique_values.append(v)

    return len(unique_values)

if __name__ == "__main__":
    import doctest
    doctest.testmod()