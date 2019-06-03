def kilometers_into_miles(kilometers:float) -> float:
    """
    convert kilometers into miles (1.6km per mile)
    
    >>> kilometers_into_miles(160)
    100
    >>> kilometers_into_miles(120)
    75
    """
    return kilometers / 1.6

print(kilometers_into_miles(160))
print(kilometers_into_miles(120))
