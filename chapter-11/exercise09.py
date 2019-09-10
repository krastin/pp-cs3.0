from typing import Dict

def dict_intersect(dict1: Dict, dict2: Dict) -> Dict:
    """takes two dictionaries as argument
    and returns a dictionary that contains only the key/value pairs
    found in both of the original dictionaries
    >>> a = {'a': 1, 'b': 2, 'c': 3};
    >>> b = {'b': 2, 'c': 5, 'd': 6, 'e': 7};
    >>> dict_intersect(a,b)
    {'b': 2}
    """
    intersection = {}
    smaller_dictionary = dict1 if len(dict1) <= len(dict2) else dict2
    longer_dictionary = dict2 if len(dict1) <= len(dict2) else dict1
    for k,v in smaller_dictionary.items():
        if k in longer_dictionary and longer_dictionary[k] == v:
            intersection[k] = v
    return intersection

if __name__ == "__main__":
    import doctest
    doctest.testmod()