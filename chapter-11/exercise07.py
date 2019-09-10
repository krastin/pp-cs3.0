from typing import Dict

def count_duplicates(sample_dict: Dict) -> int:
    """takes a single dictionary as an argument and returns the number of values that appear two or more times
    >>> sample_dict = {'red': 1, 'green': 1, 'blue': 2, 'purple': 2, 'black': 3, 'magenta': 4}
    >>> count_duplicates(sample_dict)
    2
    """
    seen_values = []
    duplicate_values = 0
    for k,v in sample_dict.items():
        if v not in seen_values:
            seen_values.append(v)
        else:
            duplicate_values += 1
    return duplicate_values

if __name__ == "__main__":
    import doctest
    doctest.testmod()