from typing import List

def dutch_flag(colors: List) -> List:
    """ given a list of strings, each of which is either 'red', 'green', or 'blue'
    (each is repeated several times in the list), rearrange the list so that the
    strings are in the order of the Dutch national flag:
    all the 'red' strings first, then all the 'green' strings, then all the 'blue' strings.
    btw the dutch flag colors are not red green and blue... go figure what the book author thought
    >>> colors = ['red', 'green', 'red', 'green', 'red', 'green', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green', 'red']
    >>> dutch_flag(colors)
    ['red', 'red', 'red', 'red', 'red', 'red', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue']
    """
    red = 0
    green = 0
    blue = 0
    for color in colors:
        if color == 'red': red += 1 
        if color == 'green': green  += 1 
        if color == 'blue': blue += 1 
    return ['red']*red + ['green']*green + ['blue']*blue

if __name__ == "__main__":
    import doctest
    doctest.testmod()