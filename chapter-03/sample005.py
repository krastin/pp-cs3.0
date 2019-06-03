def f(x):
    x = 2 * x

res = f(3)
res

print(res)
print(id(res))


def f(x):
    x = 2 * x
    return None

print(f(3))

def pie_percent(n: int) -> int:
    """Precondition: n > 0
    Assuming there are n people who want to eat a pie, return the percentage
    of the pie that each person gets to eat.
    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """
    return int(100 / n)

