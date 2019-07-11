import math

def myfloor(number: float) -> int:
    """We take as input a real number and give as output the greatest integer less than or equal to the number 

    >>> myfloor(2.4)
    2
    >>> myfloor(2)
    2
    >>> myfloor(2.0)
    2
    >>> myfloor(-3.1)
    -4
    """

    #if number >= 0:
    #    return int(number)
    #else:
    #    if (abs(number) - int(abs(number)) > 0):
    #        return int(number) - 1
    #    else:
    #        return int(number)

    return math.floor(number)

def absolute_round(number: float) -> int:
    """ Rounds the value of number and then produces the absolute value of that result

    >>> absolute_round(-2.1)
    2
    >>> absolute_round(3.4)
    3
    >>> absolute_round(3.7)
    4
    >>> absolute_round(-2.9)
    3
    """

    return abs(round(number))

def sine_ceiling(number: float) -> int:
    """ produces the ceiling of the sine of number

    >>> sine_ceiling(34.5)
    1
    """
    return math.ceil(math.sin(number))

if __name__ == "__main__":
    print(myfloor(-2.8))
    print(absolute_round(-4.3))
    print(sine_ceiling(34.5))