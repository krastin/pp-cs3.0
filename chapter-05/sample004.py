def is_positive(x: float) -> bool:
    """Return True iff x is positive.

    >>> is_positive(3)
    True
    >>> is_positive(-4.6)
    False
    """
    return x > 0

print(is_positive(3))
print(is_positive(-4.6))
print(is_positive(0))
